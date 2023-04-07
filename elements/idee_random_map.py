import pygame
import random

# Taille de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Taille des cases
CELL_SIZE = 20

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonction pour générer une carte aléatoire
def generate_map():
    map = []
    for i in range(SCREEN_HEIGHT // CELL_SIZE):
        row = []
        for j in range(SCREEN_WIDTH // CELL_SIZE):
            if random.random() < 0.2:
                row.append(1)
            else:
                row.append(0)
        map.append(row)
    return map

# Fonction pour dessiner la carte sur l'écran
def draw_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                pygame.draw.rect(screen, BLUE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Génération et affichage de la carte
    map = generate_map()
    draw_map(map)
    
    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()