import os
import sys
from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame as pytmx_load_pygame

def resource_path(relative_path):
    """Get absolute path to resource"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# IMPORT FUNCTIONS
def import_image(*path, alpha=True, format='png'):
    relative_path = join(*path) + f'.{format}'
    full_path = resource_path(relative_path)
    surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
    return surf

def import_folder(*path):
    frames = []
    full_path = resource_path(join(*path))
    for folder_path, sub_folders, image_names in walk(full_path):
        for image_name in sorted(image_names, key=lambda name: int(name.split('.')[0]) if name.split('.')[0].isdigit() else 0):
            file_path = join(folder_path, image_name)
            surf = pygame.image.load(file_path).convert_alpha()
            frames.append(surf)
    return frames

def import_folder_dict(*path):
    frames = {}
    full_path = resource_path(join(*path))
    for folder_path, sub_folders, image_names in walk(full_path):
        for image_name in image_names:
            file_path = join(folder_path, image_name)
            surf = pygame.image.load(file_path).convert_alpha()
            frames[image_name.split('.')[0]] = surf
    return frames

def import_sub_folders(*path):
    frames = {}
    full_path = resource_path(join(*path))
    for _, sub_folders, __ in walk(full_path):
        if sub_folders:
            for sub_folder in sub_folders:
                frames[sub_folder] = import_folder(*path, sub_folder)
    return frames

def import_tilemap(cols, rows, *path):
    frames = {}
    surf = import_image(*path)
    cell_width, cell_height = surf.get_width() / cols, surf.get_height() / rows
    for col in range(cols):
        for row in range(rows):
            cutout_rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            cutout_surf = pygame.Surface((cell_width, cell_height))
            cutout_surf.fill('green')
            cutout_surf.set_colorkey('green')
            cutout_surf.blit(surf, (0, 0), cutout_rect)
            frames[(col, row)] = cutout_surf
    return frames

def character_importer(cols, rows, *path):
    frame_dict = import_tilemap(cols, rows, *path)
    new_dict = {}
    for row, direction in enumerate(('down', 'left', 'right', 'up')):
        new_dict[direction] = [frame_dict[(col, row)] for col in range(cols)]
        new_dict[f'{direction}_idle'] = [frame_dict[(0, row)]]
    return new_dict

def all_character_import(*path):
    new_dict = {}
    full_path = resource_path(join(*path))
    for _, __, image_names in walk(full_path):
        for image in image_names:
            image_name = image.split('.')[0]
            new_dict[image_name] = character_importer(4, 4, *path, image_name)
    return new_dict

def coast_importer(cols, rows, *path):
    frame_dict = import_tilemap(cols, rows, *path)
    new_dict = {}
    terrains = ['grass', 'grass_i', 'sand_i', 'sand', 'rock', 'rock_i', 'ice', 'ice_i']
    sides = {
        'topleft': (0, 0), 'top': (1, 0), 'topright': (2, 0),
        'left': (0, 1), 'right': (2, 1), 'bottomleft': (0, 2),
        'bottom': (1, 2), 'bottomright': (2, 2)
    }
    for index, terrain in enumerate(terrains):
        new_dict[terrain] = {}
        for key, pos in sides.items():
            new_dict[terrain][key] = [frame_dict[(pos[0] + index * 3, pos[1] + row)] for row in range(0, rows, 3)]
    return new_dict

def tmx_importer(*path):
    """Import TMX maps - use default loader for embedded tilesets"""
    tmx_dict = {}
    root_folder = resource_path(join(*path))
    
    # print(f"Loading TMX files from: {root_folder}")
    
    for folder_path, _, file_names in walk(root_folder):
        for file in file_names:
            if file.endswith('.tmx'):
                full_path = join(folder_path, file)
                map_name = file.split('.')[0]
                
                # print(f"Loading map: {map_name}")
                
                try:
                    # Use default pygame image loader (no custom loader needed)
                    tmx_dict[map_name] = pytmx_load_pygame(
                        full_path,
                        pixelalpha=True
                    )
                    # print(f"✅ Successfully loaded: {map_name}")
                except Exception as e:
                    # print(f"❌ Failed to load {map_name}: {e}")
                    import traceback
                    traceback.print_exc()
    
    return tmx_dict

def audio_importer(*path):
    files = {}
    full_path = resource_path(join(*path))
    for folder_path, _, file_names in walk(full_path):
        for file_name in file_names:
            file_path = join(folder_path, file_name)
            files[file_name.split('.')[0]] = pygame.mixer.Sound(file_path)
    return files

def check_connection(radius, entity, target, tolerance=30):
    relation = vector(target.rect.center) - vector(entity.rect.center)
    if relation.length() < radius:
        if entity.facing_direction == 'left' and relation.x < 0 and abs(relation.y) < tolerance or\
           entity.facing_direction == 'right' and relation.x > 0 and abs(relation.y) < tolerance or\
           entity.facing_direction == 'up' and relation.y < 0 and abs(relation.x) < tolerance or\
           entity.facing_direction == 'down' and relation.y > 0 and abs(relation.x) < tolerance:
            return True

# GAME FUNCTIONS
def draw_bar(surface, rect, value, max_value, color, bg_color, radius=1):
    ratio = rect.width / max_value
    bg_rect = rect.copy()
    progress = max(0, min(rect.width, value * ratio))
    progress_rect = pygame.FRect(rect.topleft, (progress, rect.height))
    pygame.draw.rect(surface, bg_color, bg_rect, 0, radius)
    pygame.draw.rect(surface, color, progress_rect, 0, radius)