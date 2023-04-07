import random

# Dimensions de la carte (sans les murs)
MAP_WIDTH = 20
MAP_HEIGHT = 20

# Probabilité qu'une case soit un mur
WALL_PROBABILITY = 0.2

# Dimensions de la carte (avec les murs)
TOTAL_WIDTH = MAP_WIDTH + 2
TOTAL_HEIGHT = MAP_HEIGHT + 2

# Matrice représentant la carte
map = []

# Ajout des murs extérieurs
for i in range(TOTAL_HEIGHT):
    if i == 0 or i == TOTAL_HEIGHT - 1:
        row = [1] * TOTAL_WIDTH
    else:
        row = [1] + [0] * MAP_WIDTH + [1]
    map.append(row)

# Remplissage de la matrice avec des murs et des espaces vides
for i in range(1, TOTAL_HEIGHT - 1):
    for j in range(1, TOTAL_WIDTH - 1):
        if random.random() < WALL_PROBABILITY:
            map[i][j] = 1
        else:
            map[i][j] = 0

# Affichage de la carte
for i in range(TOTAL_HEIGHT):
    for j in range(TOTAL_WIDTH):
        print(map[i][j], end="")
    print("")