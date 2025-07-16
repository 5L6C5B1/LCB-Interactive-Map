import pygame
import pygame_menu
from button import Button
from settings import *
from game_data import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite, AnimatedSprite, BorderSprite, CollidableSprite, TransitionSprite
from entities import Player, Character
from groups import AllSprites
from dialog import DialogTree
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

        # Course Index (UOE)

        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()
        self.transition_sprites = pygame.sprite.Group()

        # Transition / Tint
        self.transition_target = None
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_mode = 'untint'
        self.tint_progress = 0
        self.tint_direction = -1
        self.tint_speed = 600        

        self.import_assets()
        self.setup(self.tmx_maps['main_3_reception'], 'spawn')

        # OVERLAYS
        self.dialog_tree = None

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
        # Clear map when transitioning
        for group in (self.all_sprites, self.collision_sprites, self.transition_sprites, self.character_sprites):
            group.empty()

        # Floor & Furnishing
        for layer in ['Floor', 'Furnishing']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

         # Transitions
        for obj in tmx_map.get_layer_by_name('Transition'):
            TransitionSprite((obj.x, obj.y), (obj.width, obj.height), (obj.properties['target'], obj.properties['pos']), self.transition_sprites)

        # Collisions
        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)
        
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
                
# DIALOG SYSTEM 
    def input(self):
        if not self.dialog_tree:
            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_SPACE]:
                for character in self.character_sprites:
                    if check_connection(100, self.player, character):
                        self.player.block() # BLOCK PLAYER INPUT
                        character.change_facing_direction(self.player.rect.center) # ENTITIES FACE EACH OTHER
                        self.create_dialog(character) # CREATE DIALOG
                        character.can_rotate = False

            if keys[pygame.K_z]:
                self.index_open = not self.index_open
                self.player.blocked = not self.player.blocked

    def create_dialog(self, character):
        if not self.dialog_tree:
            self.dialog_tree = DialogTree(character, self.player, self.all_sprites, self.fonts['dialog'], self.end_dialog)

    def end_dialog(self, character):
        self.dialog_tree = None
        self.player.unblock()
    
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

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            self.display_surface.fill('black')
            play_mouse_pos = pygame.mouse.get_pos()

            # play_back = Button(image=None, pos=(640,460),
            #                    text_input='BACK', font=self.fonts['regular'], base_color=COLORS['white'], hover_color=COLORS['gold'])
            
            # play_back.changeColor(play_mouse_pos)
            # play_back.update(self.display_surface)

            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if play_back.checkInput(play_mouse_pos):
                #         game.main_menu()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

            # Game Logic
            self.input()
            self.transition_check()
            self.all_sprites.update(dt)

            # Drawing
            self.all_sprites.draw(self.player)

            # OVERLAYS
            if self.dialog_tree: self.dialog_tree.update()

            self.tint_screen(dt)
            pygame.display.update()

    def howTo(self):
        while True:
            self.display_surface.blit(howToBG, (0,0))

            howTo_mouse_pos = pygame.mouse.get_pos()

            # howTo_text = self.fonts['bold'].render('add background image of play controls', True, COLORS['black'])
            # howTo_rect = howTo_text.get_rect(center=(640,260))
            # self.display_surface.blit(howTo_text, howTo_rect)

            howTo_back = Button(image=None, pos=(640,460), text_input='BACK', font=self.fonts['regular'], 
            base_color=COLORS['black'], hover_color=COLORS['gold'])

            howTo_back.changeColor(howTo_mouse_pos)
            howTo_back.update(self.display_surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if howTo_back.checkInput(howTo_mouse_pos):
                        game.main_menu()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

            pygame.display.update()
                
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
