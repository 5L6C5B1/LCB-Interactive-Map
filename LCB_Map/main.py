import pygame
import pygame_menu
import datetime
import subprocess
import sys
from pathlib import Path
from button import Button
from settings import *
from game_data import *
from pytmx.util_pygame import load_pygame
from os.path import join
from timer import Timer

from sprites import Sprite, AnimatedSprite, BorderSprite, CollidableSprite, TransitionSprite, BlockedSprite
from entities import Player, Character
from groups import AllSprites
from dialog import DialogTree, DialogSprite
from course_index import CourseIndex

from support import *
from course import Course

icon = pygame.image.load('graphics/icons/lcblogo.png')
bg = pygame.image.load('graphics/backgrounds/background.png')
howToBG = pygame.image.load('graphics/backgrounds/howtoplay.png')


fullscreen = False

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_icon(icon)
        pygame.display.set_caption('LCB Interactive Map | Press F11 to toggle fullscreen')
        self.clock = pygame.time.Clock()

        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()
        self.transition_sprites = pygame.sprite.Group()
        self.blocked_sprites = pygame.sprite.Group()

        # Blocked Collisions
        self.blocked_dialog = None  # Track blocked dialog state
        self.blocked_dialog_timer = Timer(1500)  # Auto-hide dialog

        # Transition / Tint
        self.transition_target = None
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_mode = 'untint'
        self.tint_progress = 0
        self.tint_direction = -1
        self.tint_speed = 600

        # Pause Menu
        self.paused = False
        self.pause_menu_alpha = 0
        self.pause_fade_speed = 400
        
        self.import_assets()
        # DEBUG: Print what icons were loaded
        print("Icons loaded:", list(self.course_frames['icons'].keys()))
        self.setup(self.tmx_maps['main_3_reception'], 'spawn')

        # Overlays
        self.dialog_tree = None
        self.course_index = CourseIndex(UNIVERSITY_PARTNERS, COURSE_DATA, self.fonts, self.course_frames['ui'], self.course_frames['icons'])
        self.index_open = False

        # Minigames
        self.minigame_active = False
        self.minigame_callback = None

    def toggle_fullscreen(self):
        global fullscreen
        fullscreen = not fullscreen
        if fullscreen:
            self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
        else:
            self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def import_assets(self):
        self.tmx_maps = tmx_importer('data', 'maps')

        self.overworld_frames = {
            'characters': all_character_import('graphics', 'characters')
        }

        self.course_frames = {
            'icons': import_folder_dict('graphics', 'icons'),
            'courses': import_folder_dict('graphics', 'icons'),
            'ui': import_folder_dict('graphics', 'ui')
        }

        self.fonts = {
            'menu title': pygame.font.Font(join('graphics', 'fonts', 'VT323-Regular.ttf'), 90),
            'menu regular': pygame.font.Font(join('graphics', 'fonts', 'dogicapixel.otf'), 18),
            'dialog': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'), 30),
            'regular': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'), 18),
            'small': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'), 14),
            'bold': pygame.font.Font(join('graphics', 'fonts', 'dogicapixelbold.otf'), 20)
        }

        self.audio = audio_importer('audio')

    def setup(self, tmx_map, player_start_pos):
        # Get room name
        self.current_room_name = tmx_map.properties.get('display_name', '')
        self.current_room_title = tmx_map.properties.get('display_title', '')

        # Clear map when transitioning
        for group in (self.all_sprites, self.collision_sprites, self.transition_sprites, self.character_sprites):
            group.empty()

        # DEBUG: Check for missing tiles before creating sprites
        print(f"Debugging map: {tmx_map}")
        for layer in tmx_map.visible_layers:
            if hasattr(layer, 'data'):
                print(f"Checking layer: {layer.name}")
                for x, y, gid in layer:
                    if gid != 0:  # 0 means empty tile
                        surf = tmx_map.get_tile_image_by_gid(gid)
                        if surf is None:
                            print(f"Missing tile: GID {gid} at ({x}, {y}) in layer '{layer.name}'")

        # Floor & Furnishing (with safety check)
        for layer in ['Floor', 'Furnishing']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                if surf is None:
                    print(f"Skipping None surface at ({x}, {y}) in layer '{layer}'")
                    continue  # Skip creating sprite for missing tiles
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        # Transitions
        for obj in tmx_map.get_layer_by_name('Transition'):
            #debug for transition errors
            # print(f"Transition object at ({obj.x}, {obj.y})")
            # print(f"  Available properties: {list(obj.properties.keys())}")
            # print(f"  Object name: {getattr(obj, 'name', 'unnamed')}")
            
            # if 'target' not in obj.properties:
            #     print(f"  ERROR: Missing 'target' property!")
            #     continue
            
            # if 'pos' not in obj.properties:
            #     print(f"  ERROR: Missing 'pos' property!")
            #     continue
            TransitionSprite((obj.x, obj.y), (obj.width, obj.height), (obj.properties['target'], obj.properties['pos']), self.transition_sprites)

        self.blocked_sprites.empty()

        # Collisions + Blocked Collisions
        for obj in tmx_map.get_layer_by_name('Collisions'):
            if obj.properties.get('collision_type') == 'blocked':
            # Check which type of blocked collision this is and get the message
                message_type = None
                message_text = "You can't go there!"  # Default message
                
                if 'inaccessible' in obj.properties and obj.properties['inaccessible']:
                    message_type = 'inaccessible'
                    message_text = obj.properties['inaccessible']
                elif 'fire_exit' in obj.properties and obj.properties['fire_exit']:
                    message_type = 'fire_exit'
                    message_text = obj.properties['fire_exit']
                elif 'office' in obj.properties and obj.properties['office']:
                    message_type = 'office'
                    message_text = obj.properties['office']
                elif 'restroom' in obj.properties and obj.properties['restroom']:
                    message_type = 'restroom'
                    message_text = obj.properties['restroom']
                elif 'stairs' in obj.properties and obj.properties['stairs']:
                    message_type = 'stairs'
                    message_text = obj.properties['stairs']
                elif 'store' in obj.properties and obj.properties['store']:
                    message_type = 'store'
                    message_text = obj.properties['store']
                elif 'basement' in obj.properties and obj.properties['basement']:
                    message_type = 'basement'
                    message_text = obj.properties['basement']
                elif 'kitchen' in obj.properties and obj.properties['kitchen']:
                    message_type = 'kitchen'
                    message_text = obj.properties['kitchen']
                elif 'surau' in obj.properties and obj.properties['surau']:
                    message_type = 'surau'
                    message_text = obj.properties['surau']
                
                # print(f"Creating blocked sprite with message: {message_text}") # Debug
                BlockedSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), 
                            self.blocked_sprites, message_type, message_text)
            else:
                BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), 
                            self.collision_sprites)
        
        # Entities
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y), 
                        frames = self.overworld_frames['characters']['player'], 
                        groups = self.all_sprites,
                        facing_direction = obj.properties['direction'],
                        collision_sprites = self.collision_sprites)
            else:
                Character(
                        pos = (obj.x, obj.y), 
                        frames = self.overworld_frames['characters'][obj.properties['graphic']],
                        groups = (self.all_sprites, self.collision_sprites, self.character_sprites),
                        facing_direction = obj.properties['direction'],
                        character_data = CHARACTER_DATA[obj.properties['character_id']],
                        player = self.player,
                        create_dialog = self.create_dialog,
                        collision_sprites = self.collision_sprites,
                        radius = obj.properties['radius'],
                        notice_sound = self.audio['notice'])
                
    def input(self):
        keys = pygame.key.get_just_pressed()

        # Pause menu handling
        if keys[pygame.K_ESCAPE]:
            self.toggle_pause()
            return
        
        # Course index input (when index is open, handle its navigation)
        if self.index_open:
            self.course_index.input()
            
            # Close course index with X or TAB
            if keys[pygame.K_x] or keys[pygame.K_TAB]:
                self.index_open = False
                self.player.blocked = False
            return

        # If not paused, able to interact with NPC for dialog
        if not self.paused and not self.dialog_tree:
            if keys[pygame.K_SPACE] or keys[pygame.K_e] or keys[pygame.K_z]:
                for character in self.character_sprites:
                    if check_connection(100, self.player, character):
                        self.player.block() # BLOCK PLAYER INPUT
                        character.change_facing_direction(self.player.rect.center) # ENTITIES FACE EACH OTHER
                        self.create_dialog(character) # CREATE DIALOG
                        character.can_rotate = False

            if keys[pygame.K_x] or keys[pygame.K_TAB]:
                self.index_open = not self.index_open
                self.player.blocked = not self.player.blocked

    # Pause menu
    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.player.block()
        else:
            self.player.unblock()

    def handle_pause_menu(self, dt):
        if not self.paused:
            return
        
        # Menu options positions (centered)
        center_x = WINDOW_WIDTH // 2
        center_y = WINDOW_HEIGHT // 2
        
        # Create buttons
        btn_image = import_image('graphics', 'ui', 'button_rect')
        btn_image = pygame.transform.scale(btn_image, (250, 50))
        
        continue_btn = Button(image=btn_image, pos=(center_x, 346.5),
                            text_input='CONTINUE', font=self.fonts['regular'], 
                            base_color=COLORS['normal'], hover_color=COLORS['dark'])
        
        main_menu_btn = Button(image=btn_image, pos=(center_x, 413.2),
                            text_input='MAIN MENU', font=self.fonts['regular'], 
                            base_color=COLORS['normal'], hover_color=COLORS['dark'])
        
        exit_btn = Button(image=btn_image, pos=(center_x, 480),
                        text_input='EXIT TO DESKTOP', font=self.fonts['regular'], 
                        base_color=COLORS['normal'], hover_color=COLORS['dark'])
        
        # Get mouse position for hover
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]  # Left mouse button
        keys = pygame.key.get_pressed()
        
        # Handle button clicks
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.toggle_pause()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                if continue_btn.checkInput(mouse_pos):
                    self.toggle_pause()
                elif main_menu_btn.checkInput(mouse_pos):
                    # Reset game state before going to main menu
                    self.paused = False
                    self.player.unblock()  # Make sure player is unblocked
                    self.dialog_tree = None  # Clear any dialog
                    self.index_open = False  # Close index
                    # Reset any other game state as needed
                    game.main_menu()
                elif exit_btn.checkInput(mouse_pos):
                    pygame.quit()
                    exit()
        
        # Draw and update button colors
        for button in [continue_btn, main_menu_btn, exit_btn]:
            button.changeColor(mouse_pos)
        
        # Draw semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.display_surface.blit(overlay, (0, 0))
        
        # Draw pause menu background
        menu_width, menu_height = 700, 500
        menu_x = center_x - menu_width / 2
        menu_y = center_y - menu_height / 2
        
        pause_bg_rect = pygame.FRect((menu_x, menu_y), (menu_width, menu_height))
        pygame.draw.rect(self.display_surface, COLORS.get('navy', (0, 50, 100)), pause_bg_rect, 0, 12, 12, 12, 12)
        
        # Draw "PAUSED" title
        pause_text = self.fonts['menu title'].render('PAUSED', True, COLORS['white'])
        pause_rect = pause_text.get_rect(center=(center_x, 220.7))
        self.display_surface.blit(pause_text, pause_rect)
        
        # Draw current date/time
        current_time = datetime.datetime.now().strftime("%Y/%m/%d - %H:%M")
        time_text = self.fonts['small'].render(current_time, True, COLORS['white'])
        time_rect = time_text.get_rect(center=(center_x, center_y - 90))
        self.display_surface.blit(time_text, time_rect)
        
        # Draw buttons
        for button in [continue_btn, main_menu_btn, exit_btn]:
            button.update(self.display_surface)

    def end_dialog(self, character):
        self.dialog_tree = None
        self.player.unblock()
    
    def check_blocked(self):
        if not self.blocked_dialog:  # Only check if no dialog is currently showing
            for blocked_sprite in self.blocked_sprites:
                if self.player.hitbox.colliderect(blocked_sprite.rect):
                    # print(f"Player collided with blocked sprite: {blocked_sprite.message_text}")  # Debug
                    self.show_blocked_dialog(blocked_sprite.message_text)
                    break

    def show_blocked_dialog(self, message_text):
        if not self.blocked_dialog and message_text:
            print(f"Showing blocked dialog: {message_text}")
            self.blocked_dialog = DialogSprite(
                message_text, 
                None,  # No character needed
                None,  # Don't add to sprite group
                self.fonts['dialog'],
                '',  # Empty speaker name for system messages (blocked collision dialogs)
                self.fonts['bold']
            )
            self.blocked_dialog_timer.activate()

    def update_blocked_dialog(self):
        if self.blocked_dialog:
            self.blocked_dialog_timer.update()
            if not self.blocked_dialog_timer.active:
                self.blocked_dialog.kill()
                self.blocked_dialog = None

    # Minigames
    def launch_minigame(self, game_name, callback):
        """Launch external minigame and store callback"""
        self.minigame_callback = callback
        self.minigame_active = True
        
        # Minigames are inside LCB_Map folder, so use relative paths from current directory
        if game_name == 'space_invaders':
            possible_paths = [
                Path('Space_Invaders/code/main.py'),
                Path('Space_Invaders/main.py'),
            ]
        elif game_name == 'breakout':
            possible_paths = [
                Path('Breakout/main.py'),
                Path('Breakout/code/main.py'),
            ]
        else:
            print(f"Unknown game: {game_name}")
            self.minigame_active = False
            if self.minigame_callback:
                self.minigame_callback('lose')
                self.minigame_callback = None
            return
        
        # Find the first path that exists
        minigame_path = None
        for path in possible_paths:
            if path.exists():
                minigame_path = path
                print(f"Found minigame at: {path.absolute()}")
                break
        
        if minigame_path is None:
            print(f"ERROR: Minigame '{game_name}' not found in any of these locations:")
            for path in possible_paths:
                print(f"  - {path.absolute()}")
            print(f"Current directory: {Path.cwd()}")
            self.minigame_active = False
            if self.minigame_callback:
                self.minigame_callback('lose')
                self.minigame_callback = None
            return
        
        try:
            print(f"Launching minigame: {minigame_path.absolute()}") # debug

            if minigame_path.parent.name == 'code':
                # If main.py is in a 'code' subfolder, go up one more level
                working_dir = minigame_path.parent.parent.absolute()
            else:
                # Otherwise use the direct parent
                working_dir = minigame_path.parent.absolute()
            
            print(f"Working directory: {working_dir}") # debug
            
            # Launch minigame as subprocess
            result = subprocess.run(
                [sys.executable, str(minigame_path.absolute())],
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
                cwd=str(working_dir)
            )
            
            print(f"Minigame exited with code: {result.returncode}")
            if result.stdout:
                print(f"Minigame stdout: {result.stdout}")
            if result.stderr:
                print(f"Minigame stderr: {result.stderr}")
            
            # Check result (minigame should exit with code 0 for win, 1 for lose)
            if result.returncode == 0:
                game_result = 'win'
            else:
                game_result = 'lose'
                
        except subprocess.TimeoutExpired:
            print("Minigame timed out")
            game_result = 'lose'
        except Exception as e:
            print(f"Error launching minigame: {e}")
            import traceback
            traceback.print_exc()
            game_result = 'lose'
        
        # Return to dialog
        self.minigame_active = False
        if self.minigame_callback:
            self.minigame_callback(game_result)
            self.minigame_callback = None

    
    def create_dialog(self, character):
        if not self.dialog_tree:
            self.dialog_tree = DialogTree(
                character, 
                self.player, 
                self.all_sprites, 
                self.fonts['dialog'],
                self.fonts['bold'],
                self.end_dialog,
                self.launch_minigame,  # minigame launcher
                self.fonts['small']
            )


    # Transitioning to other areas
    def transition_check(self):
        sprites = [sprite for sprite in self.transition_sprites if sprite.rect.colliderect(self.player.hitbox)]
        if sprites:
            self.player.block()
            self.transition_target = sprites[0].target
            self.tint_mode = 'tint'

    def tint_screen(self, dt):
        if self.tint_mode == 'untint':
            self.tint_progress -= self.tint_speed * dt

        if self.tint_mode == 'tint':
            self.tint_progress += self.tint_speed * dt
            if self.tint_progress >= 255:
                self.setup(self.tmx_maps[self.transition_target[0]], self.transition_target[1])
                self.tint_mode = 'untint'
                self.transition_target = None

        self.tint_progress = max(0, min(self.tint_progress, 255))
        self.tint_surf.set_alpha(self.tint_progress)
        self.display_surface.blit(self.tint_surf, (0,0))

    
    # Game loop
    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            self.display_surface.fill('black')

            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

                if self.index_open and event.type == pygame.MOUSEWHEEL:
                    self.course_index.handle_scroll(-event.y)

            # Game Logic
            self.input()
            if not self.paused:
                self.transition_check()
                self.check_blocked()
                self.update_blocked_dialog()
                self.all_sprites.update(dt)

            # Drawing
            self.all_sprites.draw(self.player) # Draw sprites
            if self.dialog_tree:
                if self.dialog_tree.current_dialog:
                    self.display_surface.blit(self.dialog_tree.current_dialog.image, self.dialog_tree.current_dialog.rect)
                    if hasattr(self.dialog_tree.current_dialog, 'hint_text'):
                        self.display_surface.blit(self.dialog_tree.current_dialog.hint_text, self.dialog_tree.current_dialog.hint_rect)
                if self.dialog_tree.current_choices:
                    self.display_surface.blit(self.dialog_tree.current_choices.image, self.dialog_tree.current_choices.rect)

            # Draw blocked dialog
            if self.blocked_dialog:
                self.display_surface.blit(self.blocked_dialog.image, self.blocked_dialog.rect)
                # Draw hint text for blocked dialog
                if hasattr(self.blocked_dialog, 'hint_text'):
                    self.display_surface.blit(self.blocked_dialog.hint_text, self.blocked_dialog.hint_rect)
            title_font = self.fonts['small']
            room_font = self.fonts['regular']

            # Calculate positions
            base_y = WINDOW_HEIGHT - 10
            base_x = 10

            # display_name - bottom text
            if self.current_room_name:
                room_text = room_font.render(self.current_room_name, True, COLORS['white'])
                room_y = base_y - room_text.get_height()
                
                # Draw outline (multiple directions)
                room_shadow = room_font.render(self.current_room_name, True, COLORS['black'])
                for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                    self.display_surface.blit(room_shadow, (base_x + dx, room_y + dy))
                
                self.display_surface.blit(room_text, (base_x, room_y))

            # display_title
            if self.current_room_title:
                title_text = title_font.render(self.current_room_title, True, COLORS['white'])
                title_y = room_y - title_text.get_height() - 5 if self.current_room_name else base_y - title_text.get_height()
                
                # Draw outline (multiple directions)
                title_shadow = title_font.render(self.current_room_title, True, COLORS['black'])
                for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                    self.display_surface.blit(title_shadow, (base_x + dx, title_y + dy))
                
                self.display_surface.blit(title_text, (base_x, title_y))

            # Overlays
            if not self.paused:
                if self.dialog_tree: 
                    self.dialog_tree.update()
                if self.index_open: 
                    self.course_index.update(dt)

            # Handle pause menu (this will draw over everything)
            self.handle_pause_menu(dt)

            # Tint screen (existing transition system)
            if not self.paused:  # Only do transitions when not paused
                self.tint_screen(dt)
            pygame.display.update()
  
    # How to Play menu
    def howTo(self):
        back_icon = pygame.image.load('graphics/icons/back.png')
        back_icon_resize = pygame.transform.scale(back_icon, (48, 48))

        while True:
            self.display_surface.blit(howToBG, (0,0))

            howTo_mouse_pos = pygame.mouse.get_pos()

            icon_rect = pygame.Rect(35, 35, 48, 48)  # x, y, width, height
            self.display_surface.blit(back_icon_resize, (35, 35))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if icon_rect.collidepoint(howTo_mouse_pos):
                        game.main_menu()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

            pygame.display.update()

    # Main Menu
    def main_menu(self):
        while True:
            self.display_surface.blit(bg, (0,0))

            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = self.fonts['menu title'].render('LCB Interactive', True, COLORS['navy'])
            menu2_text = self.fonts['menu title'].render('Map', True, COLORS['navy'])
            menu_rect = menu_text.get_rect(center=(640,180))
            menu2_rect = menu2_text.get_rect(center=(640, menu_rect.bottom + 30))

            btn_image = import_image('graphics', 'ui', 'button_rect')
            btn_image = pygame.transform.scale(btn_image, (310, 64))

            play_btn = Button(image=btn_image, pos=(640,430),
                              text_input='PLAY', font=self.fonts['menu regular'], base_color=COLORS['normal'], hover_color=COLORS['dark'])
            howTo_btn = Button(image=btn_image, pos=(640,510),
                               text_input='HOW TO PLAY', font=self.fonts['menu regular'], base_color=COLORS['normal'], hover_color=COLORS['dark'])
            quit_btn = Button(image=btn_image, pos=(640,590),
                              text_input='QUIT', font=self.fonts['menu regular'], base_color=COLORS['normal'], hover_color=COLORS['dark'])

            self.display_surface.blit(menu_text, menu_rect)
            self.display_surface.blit(menu2_text, menu2_rect)

            for button in [play_btn, howTo_btn, quit_btn]:
                button.changeColor(menu_mouse_pos)
                button.update(self.display_surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_btn.checkInput(menu_mouse_pos):
                        game.run()
                    if howTo_btn.checkInput(menu_mouse_pos):
                        game.howTo()
                    if quit_btn.checkInput(menu_mouse_pos):
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.main_menu()