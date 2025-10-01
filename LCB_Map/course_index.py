from settings import *
from support import draw_bar
import pygame

class CourseIndex:
    def __init__(self, university_partners, course_data, fonts, ui_frames, icon_frames):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        self.university_partners = university_partners
        self.course_data = course_data
        self.current_view = 'partners'  # 'partners' or 'courses'
        self.selected_partner = None
        self.last_key_time = 0


        # FIELD COLORS
        self.field_colors = {
            'law': '#b99671',           # grey orange
            'computer': '#a8b8c2',      # pastel grey azure
            'business': '#579685',      # grey turquoise
            'tourism': '#8ccbd8',       # azure
            'culinary': '#be1919'       # red
        }
        
        # FRAMES 
        self.ui_frames = ui_frames
        self.icon_frames = icon_frames  # Add this line
        
        # TINT SURFACE
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)
        
        # DIMENSIONS
        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.8).move_to(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
        # LIST 
        self.visible_items = 6
        self.list_width = self.main_rect.width * 0.3
        self.item_height = self.main_rect.height / self.visible_items
        self.index = 0
        
        # SCROLLING
        self.scroll_y = 0
        self.max_scroll = 0
        
        # Get current items based on view
        self.current_items = self.university_partners if self.current_view == 'partners' else self.get_partner_courses()

    def get_partner_courses(self):
        if not self.selected_partner:
            return {}
        return {name: data for name, data in self.course_data.items() 
                if data['partner'] == self.selected_partner}

    def input(self):
        keys = pygame.key.get_just_pressed()
        
        # Handle view switching
        if keys[pygame.K_SPACE]:
            if self.current_view == 'partners':
                partner_names = list(self.university_partners.keys())
                if partner_names and self.index < len(partner_names):
                    self.selected_partner = partner_names[self.index]
                    self.current_view = 'courses'
                    self.current_items = self.get_partner_courses()
                    self.index = 0
                    self.scroll_y = 0
                    
        if keys[pygame.K_BACKSPACE]:
            if self.current_view == 'courses':
                self.current_view = 'partners'
                self.current_items = self.university_partners
                self.selected_partner = None
                self.index = 0
                self.scroll_y = 0
        
        # Navigation - use get_pressed() instead of get_just_pressed()
        # but add manual debouncing
        current_time = pygame.time.get_ticks()
        if not hasattr(self, 'last_key_time'):
            self.last_key_time = 0
        
        if current_time - self.last_key_time > 150:  # 150ms debounce
            keys_held = pygame.key.get_pressed()
            
            if keys_held[pygame.K_UP] or keys_held[pygame.K_w]:
                self.index -= 1
                self.scroll_y = 0
                self.last_key_time = current_time
                
            elif keys_held[pygame.K_DOWN] or keys_held[pygame.K_s]:
                self.index += 1
                self.scroll_y = 0
                self.last_key_time = current_time

        # Clamp index to valid range
        if self.current_items:
            self.index = self.index % len(self.current_items)
        else:
            self.index = 0



    def handle_scroll(self, scroll_direction):
        """Handle mouse wheel scrolling in the details section"""
        if self.current_view == 'courses' and self.current_items:
            self.scroll_y += scroll_direction * 30
            self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))

    def wrap_text(self, text, font, max_width):
        """Wrap text to fit within max_width"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if font.size(test_line)[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # Word is too long, break it
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines

    def display_list(self):
        bg_rect = pygame.FRect(self.main_rect.topleft, (self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLORS['gray'], bg_rect, 0, 0, 12, 0, 12, 0)

        if not self.current_items:
            return

        items_list = list(self.current_items.items())
        v_offset = 0 if self.index < self.visible_items else -(self.index - self.visible_items + 1) * self.item_height
        
        for idx, (name, data) in enumerate(items_list):
            # COLOURS
            bg_color = COLORS['gray'] if self.index != idx else COLORS['light']
            text_color = COLORS['white'] if self.index != idx else COLORS['black']
            
            top = self.main_rect.top + idx * self.item_height + v_offset
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            if item_rect.colliderect(self.main_rect):
                # CHECK CORNERS
                if item_rect.collidepoint(self.main_rect.topleft):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 12)
                elif item_rect.collidepoint(self.main_rect.bottomleft + vector(1,-1)):
                    pygame.draw.rect(self.display_surface, bg_color, item_rect, 0, 0, 0, 0, 12, 0)
                else:
                    pygame.draw.rect(self.display_surface, bg_color, item_rect)
                
                # Calculate available width for text (total width minus icon area and padding)
                text_width = self.list_width - 100  # 100 = icon space (90) + padding (10)
                
                # Wrap text for the list item
                wrapped_lines = self.wrap_text(name, self.fonts['small'], text_width)
                
                # Calculate starting Y position to center text vertically in item
                total_text_height = len(wrapped_lines) * 14
                start_y = item_rect.centery - (total_text_height / 2)
                
                # Display wrapped text (limit to lines that fit in the item height)
                max_lines = int(self.item_height / 14) - 1  # Calculate how many lines fit
                for i, line in enumerate(wrapped_lines[:max_lines]):
                    text_surf = self.fonts['small'].render(line, False, text_color)
                    text_rect = text_surf.get_frect(topleft = (item_rect.left + 90, start_y + i * 14))
                    self.display_surface.blit(text_surf, text_rect)

                # Display actual icon image
                icon_name = data.get('icon', None)
                print(f"Looking for icon: {icon_name}")  # DEBUG
                if icon_name:
                    icon_surf = self.icon_frames.get(icon_name)
                    print(f"Icon surface found: {icon_surf is not None}")  # DEBUG
                    if icon_surf:
                        # Scale icon to fit (optional, adjust size as needed)
                        icon_surf = pygame.transform.scale(icon_surf, (50, 50))
                        icon_rect = icon_surf.get_frect(center = (item_rect.left + 45, item_rect.centery))
                        self.display_surface.blit(icon_surf, icon_rect)
                    else:
                        print(f"Icon '{icon_name}' not found in icon_frames")  # DEBUG
                        print(f"Available icons: {list(self.icon_frames.keys())}")  # DEBUG
                        # Fallback placeholder if icon not found
                        icon_rect = pygame.FRect(item_rect.left + 20, item_rect.centery - 25, 50, 50)
                        pygame.draw.rect(self.display_surface, COLORS['gray'], icon_rect, 0, 4)
                else:
                    # No icon specified, show placeholder
                    icon_rect = pygame.FRect(item_rect.left + 20, item_rect.centery - 25, 50, 50)
                    pygame.draw.rect(self.display_surface, COLORS['gray'], icon_rect, 0, 4)
        
        # LINES
        for i in range(1, min(self.visible_items, len(self.current_items))):
            y = self.main_rect.top + self.item_height * i
            left = self.main_rect.left
            right = self.main_rect.left + self.list_width
            pygame.draw.line(self.display_surface, COLORS['light-gray'], (left, y), (right, y))

    def display_main(self, dt):
        if not self.current_items:
            return

        items_list = list(self.current_items.items())
        if self.index >= len(items_list):
            return
            
        name, data = items_list[self.index]

        # MAIN BACKGROUND
        rect = pygame.FRect(self.main_rect.left + self.list_width, self.main_rect.top, self.main_rect.width - self.list_width, self.main_rect.height)
        pygame.draw.rect(self.display_surface, COLORS['dark'], rect, 0, 12, 0, 12, 0)
    
        if self.current_view == 'partners':
            self.display_partner_details(rect, name, data)
        else:
            self.display_course_details(rect, name, data)

    # Display initial screen
    def display_partner_details(self, rect, name, data):
        # PARTNER DISPLAY (top header area)
        top_rect = pygame.FRect(rect.topleft, (rect.width, rect.height * 0.3))
        pygame.draw.rect(self.display_surface, COLORS['white'], top_rect, 0, 0, 0, 12)

        # BANNER IMAGE (if available)
        icon_name = data.get('banner', None)
        if icon_name:
            banner_surf = self.icon_frames.get(icon_name)
            if banner_surf:
                # Scale banner to fit inside top_rect with aspect ratio preserved
                original_width, original_height = banner_surf.get_size()
                aspect_ratio = original_height / original_width

                max_width = top_rect.width * 0.8
                max_height = top_rect.height * 0.6  # Reserve some space

                new_width = max_width
                new_height = new_width * aspect_ratio

                # Scale down if too tall
                if new_height > max_height:
                    new_height = max_height
                    new_width = new_height / aspect_ratio

                scaled_banner = pygame.transform.scale(banner_surf, (int(new_width), int(new_height)))
                banner_rect = scaled_banner.get_frect(center=(top_rect.centerx, top_rect.centery))
                self.display_surface.blit(scaled_banner, banner_rect)

            else:
                # Banner not found in icon_frames — fallback to text
                name_surf = self.fonts['bold'].render(name, False, COLORS['dark'])
                name_rect = name_surf.get_frect(midtop=(top_rect.centerx, top_rect.top + 10))
                self.display_surface.blit(name_surf, name_rect)

        else:
            # No banner specified — fallback to text
            name_surf = self.fonts['bold'].render(name, False, COLORS['dark'])
            name_rect = name_surf.get_frect(midtop=(top_rect.centerx, top_rect.top + 10))
            self.display_surface.blit(name_surf, name_rect)

        # DESCRIPTION RECT BELOW TOP SECTION
        desc_rect = pygame.FRect(
            rect.left + 10,
            top_rect.bottom + 20,
            rect.width - 20,
            rect.height - top_rect.height - 40
        )

        # Wrap and render description
        wrapped_desc = self.wrap_text(data['description'], self.fonts['regular'], desc_rect.width)
        
        y_offset = 0
        for line in wrapped_desc:
            if y_offset + 25 > desc_rect.height:
                break
            text_surf = self.fonts['regular'].render(line, False, COLORS['white'])
            text_rect = text_surf.get_frect(topleft=desc_rect.topleft + vector(0, y_offset))
            self.display_surface.blit(text_surf, text_rect)
            y_offset += 25

        # PROGRAMS INFO
        if y_offset + 50 < desc_rect.height:
            y_offset += 30
            wrapped_programs = self.wrap_text(data['programs'], self.fonts['regular'], desc_rect.width)
            
            for line in wrapped_programs:
                if y_offset + 25 > desc_rect.height:
                    break
                text_surf = self.fonts['regular'].render(line, False, COLORS['white'])
                text_rect = text_surf.get_frect(topleft=desc_rect.topleft + vector(0, y_offset))
                self.display_surface.blit(text_surf, text_rect)
                y_offset += 25


    # Display list of courses under university partner
    def display_course_details(self, rect, name, data):
        # Create scrollable surface
        content_height = self.calculate_content_height(name, data, rect.width - 20)
        self.max_scroll = max(0, content_height - rect.height + 40)
        
        # COURSE TITLE SECTION
        top_rect = pygame.FRect(rect.topleft, (rect.width, rect.height * 0.25))

        # Get field color or default to blue
        field = data.get('field', 'default')
        title_color = self.field_colors.get(field, COLORS['blue'])

        pygame.draw.rect(self.display_surface, title_color, top_rect, 0, 0, 0, 12)

        # COURSE NAME
        course_lines = self.wrap_text(name, self.fonts['bold'], top_rect.width - 20)
        y_pos = 10
        for line in course_lines[:2]:  # Limit to 2 lines for title
            name_surf = self.fonts['bold'].render(line, False, COLORS['white'])
            name_rect = name_surf.get_frect(topleft = top_rect.topleft + vector(10, y_pos))
            self.display_surface.blit(name_surf, name_rect)
            y_pos += 25

        # DURATION
        duration_surf = self.fonts['regular'].render(data['duration'], False, COLORS['white'])
        duration_rect = duration_surf.get_frect(topleft = top_rect.topleft + vector(10, y_pos))
        self.display_surface.blit(duration_surf, duration_rect)

        # SCROLLABLE CONTENT AREA
        content_rect = pygame.FRect(rect.left + 10, top_rect.bottom + 10, rect.width - 20, rect.height - top_rect.height - 20)
        
        # Calculate max scroll based on actual content height
        self.max_scroll = max(0, content_height - content_rect.height)

        # Clip to content area
        clip_rect = content_rect.copy()
        self.display_surface.set_clip(clip_rect)
        
        y_offset = -self.scroll_y

        # WARNING
        if 'warning' in data and data['warning']:
            warning_lines = self.wrap_text(data['warning'], self.fonts['regular'], content_rect.width)
            for line in warning_lines:
                if y_offset > content_rect.height:
                    break
                if y_offset > -30:
                    warning_surf = self.fonts['regular'].render(line, False, COLORS['red'])
                    warning_rect = warning_surf.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                    self.display_surface.blit(warning_surf, warning_rect)
                y_offset += 22
            y_offset += 10  # Add space after warning
        
        # DESCRIPTION
        desc_lines = self.wrap_text(data['description'], self.fonts['regular'], content_rect.width)
        for line in desc_lines:
            if y_offset > content_rect.height:
                break
            if y_offset > -30:
                text_surf = self.fonts['regular'].render(line, False, COLORS['white'])
                text_rect = text_surf.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                self.display_surface.blit(text_surf, text_rect)
            y_offset += 22

        # MODULES SECTION
        y_offset += 20
        if y_offset > -30 and y_offset < content_rect.height:
            modules_title = self.fonts['bold'].render('Modules', False, COLORS['white'])
            modules_rect = modules_title.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
            self.display_surface.blit(modules_title, modules_rect)
        y_offset += 35

        for year, modules in data['modules'].items():
            if y_offset > content_rect.height:
                break

            if year.strip():
                if y_offset > -30:
                    year_surf = self.fonts['regular'].render(year, False, COLORS['light'])
                    year_rect = year_surf.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                    self.display_surface.blit(year_surf, year_rect)
                y_offset += 25

            for module in modules:
                if y_offset > content_rect.height:
                    break
                module_lines = self.wrap_text(module, self.fonts['small'], content_rect.width - 20)
                for line in module_lines:
                    if y_offset > -20:
                        module_surf = self.fonts['small'].render(line, False, COLORS['normal'])
                        module_rect = module_surf.get_frect(topleft = content_rect.topleft + vector(20, y_offset))
                        self.display_surface.blit(module_surf, module_rect)
                    y_offset += 18
            y_offset += 10

        # ENTRY REQUIREMENTS SECTION
        y_offset += 20
        if y_offset > -30 and y_offset < content_rect.height:
            req_title = self.fonts['bold'].render('Entry Requirements', False, COLORS['white'])
            req_rect = req_title.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
            self.display_surface.blit(req_title, req_rect)
        y_offset += 35

        for year, requirements in data['entry_requirements'].items():
            if y_offset > content_rect.height:
                break
            
            # Only display year header if it's not empty
            if year.strip():
                if y_offset > -30:
                    year_surf = self.fonts['regular'].render(f'{year}:', False, COLORS['light'])
                    year_rect = year_surf.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                    self.display_surface.blit(year_surf, year_rect)
                y_offset += 25

            # Handle both list and string formats
            req_list = requirements if isinstance(requirements, list) else [requirements]
            
            for req_item in req_list:
                req_lines = self.wrap_text(req_item, self.fonts['small'], content_rect.width - 20)
                for line in req_lines:
                    if y_offset > content_rect.height:
                        break
                    if y_offset > -20:
                        req_surf = self.fonts['small'].render(line, False, COLORS['gold'])
                        indent = 20 if year.strip() else 0
                        req_rect = req_surf.get_frect(topleft = content_rect.topleft + vector(indent, y_offset))
                        self.display_surface.blit(req_surf, req_rect)
                    y_offset += 18
                y_offset += 8  # Add small gap between different requirements
            
            y_offset += 7  # Additional gap after each year group

        # NOTES
        if 'notes' in data and data['notes']:
            y_offset += 20
            if y_offset > -30 and y_offset < content_rect.height:
                notes_title = self.fonts['bold'].render('Notes', False, COLORS['white'])
                notes_rect = notes_title.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                self.display_surface.blit(notes_title, notes_rect)
            y_offset += 35

            for category, note_items in data['notes'].items():
                if y_offset > content_rect.height:
                    break
                
                # Handle both list and string formats
                note_list = note_items if isinstance(note_items, list) else [note_items]
                
                for note_item in note_list:
                    note_lines = self.wrap_text(note_item, self.fonts['small'], content_rect.width - 20)
                    for line in note_lines:
                        if y_offset > content_rect.height:
                            break
                        if y_offset > -20:
                            note_surf = self.fonts['small'].render(line, False, COLORS['plant'])
                            note_rect = note_surf.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                            self.display_surface.blit(note_surf, note_rect)
                        y_offset += 18
                    y_offset += 8
                
                y_offset += 7

        # WHATS NEXT
        if 'whats_next' in data and data['whats_next']:
            y_offset += 20
            if y_offset > -30 and y_offset < content_rect.height:
                next_title = self.fonts['bold'].render('What\'s Next?', False, COLORS['white'])
                next_rect = next_title.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                self.display_surface.blit(next_title, next_rect)
            y_offset += 35

            for year, next_steps in data['whats_next'].items():
                if y_offset > content_rect.height:
                    break
                
                if year.strip():
                    if y_offset > -30:
                        year_surf = self.fonts['regular'].render(f'{year}:', False, COLORS['light'])
                        year_rect = year_surf.get_frect(topleft = content_rect.topleft + vector(0, y_offset))
                        self.display_surface.blit(year_surf, year_rect)
                    y_offset += 25

                # Handle both list and string formats
                req_list = next_steps if isinstance(next_steps, list) else [next_steps]
                
                for next_item in req_list:
                    next_lines = self.wrap_text(next_item, self.fonts['small'], content_rect.width - 20)
                    for line in next_lines:
                        if y_offset > content_rect.height:
                            break
                        if y_offset > -20:
                            next_surf = self.fonts['small'].render(line, False, COLORS['normal'])
                            indent = 20 if year.strip() else 0
                            next_rect = next_surf.get_frect(topleft = content_rect.topleft + vector(indent, y_offset))
                            self.display_surface.blit(next_surf, next_rect)
                        y_offset += 18
                    y_offset += 8  # Add small gap between different requirements
                
                y_offset += 7  # Additional gap after each year group

        # Remove clipping
        self.display_surface.set_clip(None)

    # Calculate total height of scrollable content in description
    def calculate_content_height(self, name, data, width):
        height = 0

        # Warning
        if 'warning' in data and data['warning']:
            warning_lines = self.wrap_text(data['warning'], self.fonts['regular'], width)
            height += len(warning_lines) * 22 + 10
        
        # Description
        desc_lines = self.wrap_text(data['description'], self.fonts['regular'], width)
        height += len(desc_lines) * 22 + 40
        
        # Modules
        height += 35  # Title
        for year, modules in data['modules'].items():
            height += 25  # Year title
            for module in modules:
                module_lines = self.wrap_text(module, self.fonts['small'], width - 20)
                height += len(module_lines) * 18
            height += 10  # Space after year

        # Entry Requirements
        height += 55  # Title + space
        for year, requirements in data['entry_requirements'].items():
            if year.strip():
                height += 25  # Year title
            
            # Handle both list and string formats
            req_list = requirements if isinstance(requirements, list) else [requirements]
            
            for req_item in req_list:
                req_lines = self.wrap_text(req_item, self.fonts['small'], width - 20)
                height += len(req_lines) * 18 + 8  # 8px gap between requirements
            
            height += 7  # Additional gap after year group

        # Notes
        if 'notes' in data and data['notes']:
            height += 55
            for category, note_items in data['notes'].items():
                note_list = note_items if isinstance(note_items, list) else [note_items]
                
                for note_item in note_list:
                    note_lines = self.wrap_text(note_item, self.fonts['small'], width - 20)
                    height += len(note_lines) * 18 + 8
                
                height += 7

        # Whats's Next
        if 'whats_next' in data and data['whats_next']:
            height += 55  # Title + space
            for category, next_steps in data['whats_next'].items():
                next_list = next_steps if isinstance(next_steps, list) else [next_steps]
                
                for next_item in next_list:
                    next_lines = self.wrap_text(next_item, self.fonts['small'], width - 20)
                    height += len(next_lines) * 18 + 8
                
                height += 7

        return height

    # Display navigation controls beside index
    def display_navigation_help(self):
        """Display navigation instructions"""
        help_rect = pygame.FRect(self.main_rect.right + 20, self.main_rect.top, 200, 200)
        pygame.draw.rect(self.display_surface, COLORS['gray'], help_rect, 0, 8)
        
        help_title = self.fonts['regular'].render('Navigation:', False, COLORS['white'])
        help_title_rect = help_title.get_frect(topleft = help_rect.topleft + vector(10, 10))
        self.display_surface.blit(help_title, help_title_rect)
        
        instructions = [
            '↑/↓ or W/S - Navigate list',
            'SPACE - Select/View courses', 
            'BACKSPACE - Back to partners',
            'MOUSE WHEEL - Scroll details'
        ]
        
        y_pos = 35
        for instruction in instructions:
            # Wrap each instruction line
            wrapped_lines = self.wrap_text(instruction, self.fonts['small'], help_rect.width - 20)
            
            for line in wrapped_lines:
                inst_surf = self.fonts['small'].render(line, False, COLORS['red'])
                inst_rect = inst_surf.get_frect(topleft = help_rect.topleft + vector(10, y_pos))
                self.display_surface.blit(inst_surf, inst_rect)
                y_pos += 16  # Slightly smaller spacing for wrapped lines
            
            y_pos += 4  # Add a small gap between different instructions

    def update(self, dt):
        self.input()
        self.display_surface.blit(self.tint_surf, (0,0))
        self.display_list()
        self.display_main(dt)
        self.display_navigation_help()