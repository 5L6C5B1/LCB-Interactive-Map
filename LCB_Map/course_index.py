from settings import *
from game_data import COURSE_DATA

class CourseIndex:
    def __init__(self, fonts, courses, course_frames):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        self.courses = courses

        # Frames
        self.icon_frames = course_frames['icons']
        self.course_frames = course_frames['course']
        self.ui_frames = course_frames['ui']

        # Tint Surface
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)

        # Dimensions
        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.8).move_to(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # List
        self.visible_items = 6 #alter this as a scroll function will be added
        self.list_width = self.main_rect.width * 0.3
        self.item_height = self.main_rect.height
        self.index = 0
        self.selected_index = None

    def input(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_UP or pygame.K_w]: # add mouse interactivity (mouse wheel scrolling/mouse clicking)
            self.index -= 1
        if keys[pygame.K_DOWN or pygame.K_s]:
            self.index += 1

        self.index = self.index % len(self.courses)

    def display_list(self):
        bg_rect = pygame.FRect(self.main_rect.topleft, (self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLORS['gray'], bg_rect, 0, 0, 12, 0, 12, 0)

        v_offset = 0 if self.index < self.visible_items else -(self.index - self.visible_items +1) * self.item_height
        for index, course in self.courses.items():
            # Colours
            bg_color = COLORS['gray'] if self.index != index else COLORS['light']
            text_color = COLORS['white'] if self.index != index else COLORS['black']

            top = self.main_rect.top + index * self.item_height + v_offset
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            text_surf = self.fonts['regular'].render(course.name, False, text_color)
            text_rect = text_surf.get_frect(midleft = item_rect.midleft + vector(90,0))

            icon_surf = self.icon_frames[course.name]
            icon_rect = icon_surf.get_frect(center = item_rect.midleft + vector(45,0))

            if item_rect.colliderect(self.main_rect):
                # Check corners
                if item_rect.collidepoint(self.main_rect.topleft):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 12)
                elif item_rect.collidepoint(self.main_rect.bottomleft + vector(1,-1)):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 0, 0, 12, 0)
                else:
                    pygame.draw.rect(self.display_surface, bg_color, item_rect)

                self.display_surface.blit(text_surf, text_rect)
                self.display_surface.blit(icon_surf, icon_rect)

        # Lines
        for i in range(1, min(self.visible_items, len(self.courses))):
            y = self.main_rect.top + self.item_height * i
            left = self.main_rect.left
            right = self.main_rect.left + self.list_width
            pygame.draw.line(self.display_surface, COLORS['light-gray'], (left, y), (right, y))

    def display_main(self, dt):
        # Data
        course = self.courses[self.index]

        # Main Background
        rect = pygame.FRect(self.main_rect.left + self.list_width, self.main_rect.top, self.main_rect.width - self.list_width, self.main_rect.height)
        pygame.draw.rect(self.display_surface, COLORS['dark'], rect, 0, 12, 0, 12, 0)

        # Course Display
        top_rect = pygame.FRect(rect.topleft, (rect.width, rect.height * 0.4))
        pygame.draw.rect(self.display_surface, COLORS[course.element], top_rect, 0, 0, 0, 12)

        
        course_surf = self.course_frames[course.name]['idle'][0]
        course_rect = course_surf.get_frect(center = top_rect.center)