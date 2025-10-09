from settings import *
from timer import Timer

class DialogTree:
    def __init__(self, character, player, all_sprites, font, bold_font, end_dialog, launch_minigame_callback, hint_font=None):
        self.player = player
        self.character = character
        self.font = font
        self.bold_font = bold_font
        self.hint_font = hint_font if hint_font else font
        self.all_sprites = all_sprites
        self.end_dialog = end_dialog
        self.launch_minigame = launch_minigame_callback
        
        self.dialog_data = character.character_data['dialog']
        self.current_node = 'start'
        
        self.current_dialog = None
        self.current_choices = None
        self.dialog_timer = Timer(500, autostart=True)
        self.waiting_for_choice = False 
        
        self.show_current_node()

    def on_choice_selected(self, next_node):
        """Handle the player's choice and set the next node."""
        # Check if this triggers a minigame
        if next_node == 'launch_si':
            # Clear dialog
            if self.current_dialog:
                self.current_dialog.kill()
            if self.current_choices:
                self.current_choices.kill()
            
            # Launch Space Invaders
            self.launch_minigame('space_invaders', self.on_minigame_complete)
        elif next_node == 'launch_b':
            # Clear dialog
            if self.current_dialog:
                self.current_dialog.kill()
            if self.current_choices:
                self.current_choices.kill()
            
            # Launch Breakout
            self.launch_minigame('breakout', self.on_minigame_complete)
        else:
            self.current_node = next_node
            self.show_current_node()

    
    def on_minigame_complete(self, result):
        """Called when minigame finishes. result is 'win' or 'lose'"""
        if result == 'win':
            self.current_node = 'minigame_win'
        else:
            self.current_node = 'minigame_lose'
        self.show_current_node()

    
    def show_current_node(self):
    # Handle old-style linear dialogs
        if isinstance(self.dialog_data, dict) and 'default' in self.dialog_data:
            if self.current_dialog:
                self.current_dialog.kill()
            self.current_dialog = DialogSprite(
                self.dialog_data['default'][0], 
                self.character, 
                None,  # Don't add to any group
                self.font,
                self.character.character_data.get('name', 'NPC')
            )
            return
        
        # Handle new-style branching dialogs
        node = self.dialog_data.get(self.current_node)
        if not node:
            self.end_dialog(self.character)
            return
        
        # Clear previous dialog/choices
        if self.current_dialog:
            self.current_dialog.kill()
            self.current_dialog = None
        if self.current_choices:
            self.current_choices.kill()
            self.current_choices = None
        
        # Show text
        text = node['text']
        self.dialog_lines = text if isinstance(text, list) else [text]
        self.dialog_index = 0
        self.waiting_for_choice = False
        self.show_dialog_line()

    def show_choices(self):
        """Show choices after player reads the dialog"""
        node = self.dialog_data.get(self.current_node)
        if node and node['options']:
            # Kill the current dialog box to clear the screen
            if self.current_dialog:
                self.current_dialog.kill()
                self.current_dialog = None

            # Show the choices
            self.current_choices = DialogChoiceSprite(
                node['options'],
                self.character,
                None,  # Don't add to any group
                self.font,
                self.on_choice_selected
            )
            self.waiting_for_choice = False

    def show_dialog_line(self):
        # Clear old dialog
        if self.current_dialog:
            self.current_dialog.kill()
            self.current_dialog = None

        if self.dialog_index < len(self.dialog_lines):
            print(f"Showing dialog line {self.dialog_index + 1}/{len(self.dialog_lines)}: {self.dialog_lines[self.dialog_index]}")

            self.current_dialog = DialogSprite(
                self.dialog_lines[self.dialog_index],
                self.character,
                None,
                self.font,
                self.character.character_data.get('name', 'NPC'),
                self.bold_font,
                self.hint_font
            )
            self.dialog_timer.activate()
            self.dialog_index += 1
        else:
            # All lines shown, now move to choices or end
            node = self.dialog_data.get(self.current_node)
            if node and node['options']:
                self.show_choices()
            else:
                self.end_dialog(self.character)



    def input(self):
        if not self.dialog_timer.active:
            keys = pygame.key.get_just_pressed()
            
            if self.current_choices:
                # Navigate choices
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.current_choices.update_selection(-1)
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.current_choices.update_selection(1)
                elif keys[pygame.K_SPACE] or keys[pygame.K_e] or keys[pygame.K_z]:
                    self.current_choices.confirm_selection()
            else:
                # Advance through dialog lines
                if keys[pygame.K_SPACE] or keys[pygame.K_e] or keys[pygame.K_z]:
                    self.show_dialog_line()
    
    def update(self):
        self.dialog_timer.update()
        
        # Show next node after timer expires
        if hasattr(self, 'show_next') and not self.dialog_timer.active:
            next_node = self.show_next
            delattr(self, 'show_next')
            self.current_node = next_node
            self.show_current_node()
        
        self.input()

class DialogSprite(pygame.sprite.Sprite):
    def __init__(self, message, character, groups, font, speaker_name="NPC", bold_font=None, hint_font=None):
        super().__init__()
        self.z = WORLD_LAYERS['top']

        # Fixed size for all dialog boxes
        width = 850
        height = 200
        padding = 20
        max_text_width = width - padding * 2

        # Word wrap
        wrapped_lines = self.wrap_text(message, font, max_text_width)

        # Render wrapped lines
        line_surfaces = [font.render(line, False, COLORS['black']) for line in wrapped_lines]

        # Create background
        surf = pygame.Surface((width, height), pygame.SRCALPHA)
        surf.fill((0, 0, 0, 0))
        pygame.draw.rect(surf, COLORS['pure white'], (0, 0, width, height), 0, 4)
        pygame.draw.rect(surf, COLORS['black'], (0, 0, width, height), 2, 4)

        # Only draw speaker name if provided
        y_offset = padding
        if speaker_name:
            name_font = bold_font if bold_font else font
            name_surf = name_font.render(speaker_name.upper(), False, COLORS['dark'])
            surf.blit(name_surf, (padding, padding))
            
            # Separator line
            separator_y = padding + name_surf.get_height() + 5
            pygame.draw.line(surf, COLORS['black'], (padding, separator_y), 
                            (width - padding, separator_y), 2)
            y_offset = separator_y + 10
        else:
            # No speaker name, start text higher [system/blocked collision text]
            y_offset = padding + 10

        # Draw wrapped text
        for line_surf in line_surfaces:
            surf.blit(line_surf, (padding, y_offset))
            y_offset += line_surf.get_height() + 5

        self.image = surf
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))

        if speaker_name: 
            if hint_font is None:
                hint_font = pygame.font.Font(pygame.font.get_default_font(), 16)
            self.hint_text = hint_font.render("Press SPACE/E/Z to continue", True, COLORS['gold'])
            self.hint_rect = self.hint_text.get_rect()
            # position
            self.hint_rect.topright = (self.rect.right - 10, self.rect.top - self.hint_rect.height - 5)

    
    def wrap_text(self, text, font, max_width):
        # Wrap text to fit within max_width
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_surf = font.render(test_line, False, COLORS['black'])
            
            if test_surf.get_width() <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines if lines else [text]


class DialogChoiceSprite(pygame.sprite.Sprite):
    def __init__(self, choices, character, groups, font, on_select):
        super().__init__()
        self.z = WORLD_LAYERS['top']
        self.choices = choices
        self.selected_index = 0
        self.on_select = on_select
        self.font = font
        self.character = character

        self.render_choices()

    def render_choices(self):
        padding = 15
        line_height = 30
        line_spacing = 10
        max_lines = 4 

        # Fixed size for choices box
        width = 850
        height = padding * 2 + (line_height + line_spacing) * len(self.choices) - line_spacing

        surf = pygame.Surface((width, height), pygame.SRCALPHA)
        surf.fill((0, 0, 0, 0))
        pygame.draw.rect(surf, COLORS['light'], (0, 0, width, height), 0, 4)
        pygame.draw.rect(surf, COLORS['black'], (0, 0, width, height), 2, 4)

        for i, choice in enumerate(self.choices):
            y = padding + i * (line_height + line_spacing)

            if i == self.selected_index:
                color = COLORS['white']
                bg_color = COLORS['black']
                prefix = '→ '
            else:
                color = COLORS['black']
                bg_color = None
                prefix = '  '

            text_surf = self.font.render(prefix + choice['text'], False, color)

            if bg_color:
                bg_rect = text_surf.get_rect()
                bg_rect.topleft = (padding, y)
                pygame.draw.rect(surf, bg_color, bg_rect)

            surf.blit(text_surf, (padding, y))

        self.image = surf
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))


    
    def update_selection(self, direction):
        self.selected_index = (self.selected_index + direction) % len(self.choices)
        self.render_choices()
    
    def confirm_selection(self):
        selected_choice = self.choices[self.selected_index]
        self.on_select(selected_choice['next'])  # Call the callback with next node