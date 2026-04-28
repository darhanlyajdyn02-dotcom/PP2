import json
import os
from pathlib import Path

# --- Screen sizes and grids ---
WIDTH = 600
HEIGHT = 600
CELL = 30
GRID_W = WIDTH // CELL
GRID_H = HEIGHT // CELL

# --- Colors (RGB) ---
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
BLACK = (0, 0, 0)

# Object colors
RED = (255, 0, 0)          # Regular food
DARK_RED = (120, 0, 0)     # Poisonous food
GREEN = (0, 200, 0)        # Snake / Food +1
YELLOW = (255, 220, 0)     # The body of a snake
BLUE = (0, 100, 255)       # Speed Boost
PURPLE = (160, 0, 200)     # Slow Motion
ORANGE = (255, 140, 0)     # Shield

# --- Settings (JSON) ---
SETTINGS_FILE = Path("settings.json")

DEFAULT_SETTINGS = {
    "snake_color": [0, 255, 0],  # Default green
    "grid": True,
    "sound": True
}

def load_settings():
    """Loads settings from a file or creates default ones."""
    if not SETTINGS_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            settings = json.load(file)
        
        #Check: If the file is missing any keys, add them
        for key, value in DEFAULT_SETTINGS.items():
            if key not in settings:
                settings[key] = value
        return settings
    except (json.JSONDecodeError, Exception):
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    """Saves the current settings to settings.json."""
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)

# --- Gameplay settings---
BASE_FPS = 8
FPS_STEP = 1  # How much does speed increase with each level?
POWERUP_DURATION = 5000  # 5 seconds of bonus action
POWERUP_LIFETIME = 8000  # The bonus remains on the field for 8 seconds.