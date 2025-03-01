import pygame
import pygame_menu
from button import Button
from settings import *

from support import *

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

        self.import_assets()

    def import_assets(self):
        self.fonts = {
            'menu title': pygame.font.Font(join('graphics', 'fonts', 'VT323-Regular.ttf'), 90),
            'menu regular': pygame.font.Font(join('graphics', 'fonts', 'dogicapixel.otf'), 18),
            'dialog': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'), 30),
            'regular': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'), 18),
            'small': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'), 14),
            'bold': pygame.font.Font(join('graphics', 'fonts', 'dogicapixelbold.otf'), 20)
        }

    def toggle_fullscreen(self):
        global fullscreen
        fullscreen = not fullscreen
        if fullscreen:
            self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
        else:
            self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            play_mouse_pos = pygame.mouse.get_pos()

            self.display_surface.fill('black')

            play_text = self.fonts['bold'].render('PLAY SCREEN', True, COLORS['white'])
            play_rect = play_text.get_rect(center=(640, 260))
            self.display_surface.blit(play_text, play_rect)

            play_back = Button(image=None, pos=(640,460),
                               text_input='BACK', font=self.fonts['regular'], base_color=COLORS['white'], hover_color=COLORS['gold'])
            
            play_back.changeColor(play_mouse_pos)
            play_back.update(self.display_surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back.checkInput(play_mouse_pos):
                        game.main_menu()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

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
