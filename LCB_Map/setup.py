import os
from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base = base)]

packages = ["idna", "settings", "game_data", "pytmx.util_pygame", "sprites", "entities", "groups", 
    "dialog", "course_index", "support", "course"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': [('audio/', 'audio/'), ('data/', 'data/'), ('graphics/', 'graphics/')]
    }
}

setup(
    name = "LCB Interactive Map | Press F11 to toggle fullscreen",
    options = options,
    version = "1.0.0",
    description = 'tut',
    executables = executables
)