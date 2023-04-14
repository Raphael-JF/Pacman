"""Ce module contient toutes les constantes nécessaires au fonctionnement du programme."""

BASE_SIZE = [800,450] #échelle pour laquelle on définit les valeurs de nos widgets
TIME_TICKING = 60 #temps in game (immutable)
START_GAME_FPS = 60 #fps au démarrage du jeu

GAME_RESOLUTIONS = [
            [800,450],
            [960,540],
            [1280,720],
            [1600,900],
            [1920,1080],
        ]

INPUT_FIELD_DASH_DELAY = 0.5 # délai de disparition/apparition du curseur dans un input_field
KEYPRESS_SPAM_DELAY = 0.5 # délai avant entrée en mode spam dans un input_field
CHARS_SPAM_DELAY = 0.05 # délai entre chaque placement de caractère en mode spam dans un input_field