from settings import *
from support import draw_bar
from game_data import COURSE_DATA, UNIVERSITY_PARTNERS
from course import Course

class CourseIndex:
    def __init__(self, fonts, ui_frames):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        
        # FRAMES 
        self.icon_frames = ui_frames.get('icons', {})
        self.ui_frames = ui_frames.get('ui', {})

        # TINT SURFACE
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)
        
        # DIMENSIONS
        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.8).move_to(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # STATE MANAGEMENT
        self.view_mode = 'partners'  # 'partners' or 'courses'
        self.selected_partner = None
        
        # University partners data
        self.university_partners = UNIVERSITY_PARTNERS
        self.partner_names = list(self.university_partners.keys())
        
        # Course data
        self.courses = {}
        for course_name in COURSE_DATA.keys():
            self.courses[course_name] = Course(course_name)
        self.course_names = list(self.courses.keys())
        
        # LIST PROPERTIES
        self.visible_items = 6
        self.list_width = self.main_rect.width * 0.3
        self.item_height = self.main_rect.height / self.visible_items
        self.index = 0
        
        # SCROLL PROPERTIES FOR DETAILS
        self.scroll_offset = 0
        self.max_scroll = 0
        self.scroll_speed = 30

    def input(self):
        keys = pygame.key.get_just_pressed()
        
        if self.view_mode == 'partners':
            if keys[pygame.K_UP]:
                self.index = max(0, self.index - 1)
            if keys[pygame.K_DOWN]:
                self.index = min(len(self.partner_names) - 1, self.index + 1)
            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                # "See courses" button functionality
                self.selected_partner = self.partner_names[self.index]
                self.view_mode = 'courses'
                self.index = 0
                self.scroll_offset = 0
        
        elif self.view_mode == 'courses':
            if keys[pygame.K_UP]:
                self.index = max(0, self.index - 1)
                self.scroll_offset = 0  # Reset scroll when changing course
            if keys[pygame.K_DOWN]:
                # Filter courses for selected partner
                partner_courses = [name for name, course in self.courses.items() 
                                 if course.university == self.selected_partner]
                self.index = min(len(partner_courses) - 1, self.index + 1)
                self.scroll_offset = 0  # Reset scroll when changing course
            if keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]:
                # Go back to partners view
                self.view_mode = 'partners'
                self.index = 0
                self.scroll_offset = 0

    def handle_scroll(self, event):
        """Handle mouse wheel scrolling for course details"""
        if self.view_mode == 'courses' and event.type == pygame.MOUSEWHEEL:
            self.scroll_offset = max(0, min(self.max_scroll, 
                                          self.scroll_offset - event.y * self.scroll_speed))

    def display_partners_list(self):
        bg_rect = pygame.FRect(self.main_rect.topleft, (self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLORS['gray'], bg_rect, 0, 0, 12, 0, 12, 0)

        v_offset = 0 if self.index < self.visible_items else -(self.index - self.visible_items + 1) * self.item_height
        
        for idx, partner_name in enumerate(self.partner_names):
            # COLOURS
            bg_color = COLORS['gray'] if self.index != idx else COLORS['light']
            text_color = COLORS['white'] if self.index != idx else COLORS['black']
            
            top = self.main_rect.top + idx * self.item_height + v_offset
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            if item_rect.colliderect(self.main_rect):
                # Draw background
                if item_rect.collidepoint(self.main_rect.topleft):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 12)
                elif item_rect.collidepoint(self.main_rect.bottomleft + vector(1,-1)):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 0, 0, 12, 0)
                else:
                    pygame.draw.rect(self.display_surface, bg_color, item_rect)
                
                # Icon (placeholder colored rectangle if no icon available)
                icon_rect = pygame.FRect(0, 0, 30, 30)
                icon_rect.center = item_rect.midleft + vector(45, 0)
                partner_data = self.university_partners[partner_name]
                
                # Try to use actual icon, fallback to colored rectangle
                if partner_data['icon'] in self.icon_frames:
                    icon_surf = self.icon_frames[partner_data['icon']]
                    self.display_surface.blit(icon_surf, icon_rect)
                else:
                    # Fallback colored rectangle
                    colors = {'essex': COLORS.get('red', (200, 50, 50)), 
                             'kensington': COLORS.get('blue', (50, 50, 200)),
                             'city_guilds': COLORS.get('green', (50, 200, 50)),
                             'pearson': COLORS.get('purple', (200, 50, 200))}
                    color = colors.get(partner_data['icon'], COLORS.get('white', (255, 255, 255)))
                    pygame.draw.rect(self.display_surface, color, icon_rect, 0, 4)
                
                # Text
                text_surf = self.fonts['regular'].render(partner_name, False, text_color)
                text_rect = text_surf.get_frect(midleft = item_rect.midleft + vector(90, 0))
                self.display_surface.blit(text_surf, text_rect)

        # Draw separator lines
        for i in range(1, min(self.visible_items, len(self.partner_names))):
            y = self.main_rect.top + self.item_height * i
            left = self.main_rect.left
            right = self.main_rect.left + self.list_width
            pygame.draw.line(self.display_surface, COLORS['light-gray'], (left, y), (right, y))

    def display_courses_list(self):
        bg_rect = pygame.FRect(self.main_rect.topleft, (self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLORS['gray'], bg_rect, 0, 0, 12, 0, 12, 0)

        # Filter courses for selected partner
        partner_courses = [(name, course) for name, course in self.courses.items() 
                          if course.university == self.selected_partner]
        
        v_offset = 0 if self.index < self.visible_items else -(self.index - self.visible_items + 1) * self.item_height
        
        for idx, (course_name, course) in enumerate(partner_courses):
            # COLOURS
            bg_color = COLORS['gray'] if self.index != idx else COLORS['light']
            text_color = COLORS['white'] if self.index != idx else COLORS['black']
            
            top = self.main_rect.top + idx * self.item_height + v_offset
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            if item_rect.colliderect(self.main_rect):
                # Draw background
                if item_rect.collidepoint(self.main_rect.topleft):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 12)
                elif item_rect.collidepoint(self.main_rect.bottomleft + vector(1,-1)):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 0, 0, 12, 0)
                else:
                    pygame.draw.rect(self.display_surface, bg_color, item_rect)
                
                # Icon
                icon_rect = pygame.FRect(0, 0, 30, 30)
                icon_rect.center = item_rect.midleft + vector(45, 0)
                
                if course.element in self.icon_frames:
                    icon_surf = self.icon_frames[course.element]
                    self.display_surface.blit(icon_surf, icon_rect)
                else:
                    # Fallback colored rectangle based on element
                    element_colors = {
                        'business': COLORS.get('blue', (50, 50, 200)),
                        'technology': COLORS.get('green', (50, 200, 50)),
                        'legal': COLORS.get('red', (200, 50, 50))
                    }
                    color = element_colors.get(course.element, COLORS.get('white', (255, 255, 255)))
                    pygame.draw.rect(self.display_surface, color, icon_rect, 0, 4)
                
                # Text (truncated if too long)
                display_name = course_name
                if len(display_name) > 20:
                    display_name = display_name[:17] + "..."
                
                text_surf = self.fonts['small'].render(display_name, False, text_color)
                text_rect = text_surf.get_frect(midleft = item_rect.midleft + vector(90, 0))
                self.display_surface.blit(text_surf, text_rect)

        # Draw separator lines
        for i in range(1, min(self.visible_items, len(partner_courses))):
            y = self.main_rect.top + self.item_height * i
            left = self.main_rect.left
            right = self.main_rect.left + self.list_width
            pygame.draw.line(self.display_surface, COLORS['light-gray'], (left, y), (right, y))

    def display_partner_main(self):
        partner_data = self.university_partners[self.partner_names[self.index]]
        
        # MAIN BACKGROUND
        rect = pygame.FRect(self.main_rect.left + self.list_width, self.main_rect.top, 
                           self.main_rect.width - self.list_width, self.main_rect.height)
        pygame.draw.rect(self.display_surface, COLORS['dark'], rect, 0, 12, 0, 12, 0)
        
        # HEADER SECTION
        top_rect = pygame.FRect(rect.topleft, (rect.width, rect.height * 0.3))
        pygame.draw.rect(self.display_surface, COLORS['blue'], top_rect, 0, 0, 0, 12)
        
        # UNIVERSITY NAME
        name_surf = self.fonts['bold'].render(self.partner_names[self.index], False, COLORS['white'])
        name_rect = name_surf.get_frect(topleft = top_rect.topleft + vector(20, 20))
        self.display_surface.blit(name_surf, name_rect)
        
        # DESCRIPTION
        desc_y = top_rect.bottom + 20
        words = partner_data['description'].split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_surf = self.fonts['regular'].render(test_line, False, COLORS['white'])
            if test_surf.get_width() > rect.width - 40:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
            else:
                current_line.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        for i, line in enumerate(lines):
            line_surf = self.fonts['regular'].render(line, False, COLORS['white'])
            line_rect = line_surf.get_frect(topleft = (rect.left + 20, desc_y + i * 25))
            self.display_surface.blit(line_surf, line_rect)
        
        # PROGRAMS SECTION
        programs_y = desc_y + len(lines) * 25 + 30
        programs_title = self.fonts['bold'].render('Programs Offered:', False, COLORS['white'])
        programs_title_rect = programs_title.get_frect(topleft = (rect.left + 20, programs_y))
        self.display_surface.blit(programs_title, programs_title_rect)
        
        # Programs text
        programs_y += 35
        prog_words = partner_data['programs'].split()
        prog_lines = []
        current_line = []
        
        for word in prog_words:
            test_line = ' '.join(current_line + [word])
            test_surf = self.fonts['regular'].render(test_line, False, COLORS['white'])
            if test_surf.get_width() > rect.width - 40:
                if current_line:
                    prog_lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    prog_lines.append(word)
            else:
                current_line.append(word)
        
        if current_line:
            prog_lines.append(' '.join(current_line))
        
        for i, line in enumerate(prog_lines):
            line_surf = self.fonts['regular'].render(line, False, COLORS['white'])
            line_rect = line_surf.get_frect(topleft = (rect.left + 20, programs_y + i * 25))
            self.display_surface.blit(line_surf, line_rect)
        
        # SEE COURSES BUTTON
        button_y = rect.bottom - 60
        button_rect = pygame.FRect(rect.centerx - 75, button_y, 150, 40)
        pygame.draw.rect(self.display_surface, COLORS['light'], button_rect, 0, 5)
        button_text = self.fonts['regular'].render('SEE COURSES', False, COLORS['black'])
        button_text_rect = button_text.get_frect(center = button_rect.center)
        self.display_surface.blit(button_text, button_text_rect)

    def display_course_main(self):
        # Filter courses for selected partner
        partner_courses = [(name, course) for name, course in self.courses.items() 
                          if course.university == self.selected_partner]
        
        if not partner_courses or self.index >= len(partner_courses):
            return
            
        course_name, course = partner_courses[self.index]
        
        # MAIN BACKGROUND
        rect = pygame.FRect(self.main_rect.left + self.list_width, self.main_rect.top, 
                           self.main_rect.width - self.list_width, self.main_rect.height)
        pygame.draw.rect(self.display_surface, COLORS['dark'], rect, 0, 12, 0, 12, 0)
        
        # Create a surface for scrollable content
        content_height = 800  # Estimated content height
        self.max_scroll = max(0, content_height - rect.height)
        
        # HEADER SECTION
        top_rect = pygame.FRect(rect.topleft, (rect.width, rect.height * 0.2))
        element_colors = {
            'business': COLORS.get('blue', (50, 50, 200)),
            'technology': COLORS.get('green', (50, 200, 50)),
            'legal': COLORS.get('red', (200, 50, 50))
        }
        header_color = element_colors.get(course.element, COLORS['blue'])
        pygame.draw.rect(self.display_surface, header_color, top_rect, 0, 0, 0, 12)
        
        # COURSE NAME
        name_surf = self.fonts['bold'].render(course_name, False, COLORS['white'])
        name_rect = name_surf.get_frect(topleft = top_rect.topleft + vector(20, 10))
        self.display_surface.blit(name_surf, name_rect)
        
        # DURATION
        duration_surf = self.fonts['regular'].render(course.duration, False, COLORS['white'])
        duration_rect = duration_surf.get_frect(topleft = top_rect.topleft + vector(20, 35))
        self.display_surface.blit(duration_surf, duration_rect)
        
        # SCROLLABLE CONTENT AREA
        content_rect = pygame.FRect(rect.left, top_rect.bottom, rect.width, rect.height - top_rect.height)
        
        # Calculate current Y position for content (affected by scroll)
        current_y = content_rect.top - self.scroll_offset + 20
        
        # Only render content that's visible
        if current_y < content_rect.bottom:
            # DESCRIPTION
            desc_title = self.fonts['bold'].render('Description:', False, COLORS['white'])
            if current_y > content_rect.top - 30:
                desc_title_rect = desc_title.get_frect(topleft = (content_rect.left + 20, current_y))
                self.display_surface.blit(desc_title, desc_title_rect)
            current_y += 30
            
            # Description text
            words = course.description.split()
            lines = []
            current_line = []
            
            for word in words:
                test_line = ' '.join(current_line + [word])
                test_surf = self.fonts['regular'].render(test_line, False, COLORS['white'])
                if test_surf.get_width() > content_rect.width - 40:
                    if current_line:
                        lines.append(' '.join(current_line))
                        current_line = [word]
                    else:
                        lines.append(word)
                else:
                    current_line.append(word)
            
            if current_line:
                lines.append(' '.join(current_line))
            
            for i, line in enumerate(lines):
                line_y = current_y + i * 25
                if content_rect.top <= line_y <= content_rect.bottom:
                    line_surf = self.fonts['regular'].render(line, False, COLORS['white'])
                    line_rect = line_surf.get_frect(topleft = (content_rect.left + 20, line_y))
                    if line_rect.bottom > content_rect.top and line_rect.top < content_rect.bottom:
                        self.display_surface.blit(line_surf, line_rect)
            
            current_y += len(lines) * 25 + 30
            
            # MODULES SECTION
            if current_y < content_rect.bottom + self.scroll_offset:
                modules_title = self.fonts['bold'].render('Modules:', False, COLORS['white'])
                if current_y > content_rect.top - 30:
                    modules_title_rect = modules_title.get_frect(topleft = (content_rect.left + 20, current_y))
                    self.display_surface.blit(modules_title, modules_title_rect)
                current_y += 35
                
                for year, modules in course.modules.items():
                    if current_y > content_rect.bottom + self.scroll_offset:
                        break
                        
                    # Year header
                    if current_y > content_rect.top - 25:
                        year_surf = self.fonts['regular'].render(f'{year}:', False, COLORS['light'])
                        year_rect = year_surf.get_frect(topleft = (content_rect.left + 40, current_y))
                        if year_rect.bottom > content_rect.top and year_rect.top < content_rect.bottom:
                            self.display_surface.blit(year_surf, year_rect)
                    current_y += 25
                    
                    # Modules for this year
                    for module in modules:
                        if current_y > content_rect.bottom + self.scroll_offset:
                            break
                        if current_y > content_rect.top - 20:
                            module_surf = self.fonts['small'].render(f'- {module}', False, COLORS['white'])
                            module_rect = module_surf.get_frect(topleft = (content_rect.left + 60, current_y))
                            if module_rect.bottom > content_rect.top and module_rect.top < content_rect.bottom:
                                self.display_surface.blit(module_surf, module_rect)
                        current_y += 20
                    current_y += 10
                
                current_y += 20
            
            # ENTRY REQUIREMENTS SECTION
            if current_y < content_rect.bottom + self.scroll_offset:
                req_title = self.fonts['bold'].render('Entry Requirements:', False, COLORS['white'])
                if current_y > content_rect.top - 30:
                    req_title_rect = req_title.get_frect(topleft = (content_rect.left + 20, current_y))
                    self.display_surface.blit(req_title, req_title_rect)
                current_y += 35
                
                for req_type, requirement in course.entry_requirements.items():
                    if current_y > content_rect.bottom + self.scroll_offset:
                        break
                    if current_y > content_rect.top - 20:
                        req_surf = self.fonts['small'].render(f'{req_type}: {requirement}', False, COLORS['white'])
                        req_rect = req_surf.get_frect(topleft = (content_rect.left + 40, current_y))
                        if req_rect.bottom > content_rect.top and req_rect.top < content_rect.bottom:
                            self.display_surface.blit(req_surf, req_rect)
                    current_y += 22
                
                current_y += 20
            
            # CAREER PROSPECTS SECTION
            if current_y < content_rect.bottom + self.scroll_offset:
                career_title = self.fonts['bold'].render('Career Prospects:', False, COLORS['white'])
                if current_y > content_rect.top - 30:
                    career_title_rect = career_title.get_frect(topleft = (content_rect.left + 20, current_y))
                    self.display_surface.blit(career_title, career_title_rect)
                current_y += 35
                
                for prospect in course.career_prospects:
                    if current_y > content_rect.bottom + self.scroll_offset:
                        break
                    if current_y > content_rect.top - 20:
                        prospect_surf = self.fonts['small'].render(f'- {prospect}', False, COLORS['white'])
                        prospect_rect = prospect_surf.get_frect(topleft = (content_rect.left + 40, current_y))
                        if prospect_rect.bottom > content_rect.top and prospect_rect.top < content_rect.bottom:
                            self.display_surface.blit(prospect_surf, prospect_rect)
                    current_y += 20
        
        # Update max scroll based on actual content height
        self.max_scroll = max(0, current_y - content_rect.bottom + 50)

    def update(self, dt):
        self.input()  # INPUT
        self.display_surface.blit(self.tint_surf, (0, 0))  # TINT MAIN GAME
        
        if self.view_mode == 'partners':
            self.display_partners_list()  # DISPLAY PARTNERS LIST 
            self.display_partner_main()  # DISPLAY PARTNER INFO
        elif self.view_mode == 'courses':
            self.display_courses_list()  # DISPLAY COURSES LIST
            self.display_course_main()  # DISPLAY COURSE DETAILS