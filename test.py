# import pygame
# from pygame.locals import *
# import tkinter as tk
# from tkinter import filedialog
# import json

# # Initialisation de Pygame
# pygame.init()

# # Dimensions de la fenêtre
# window_width = 400
# window_height = 200

# # Couleurs
# black = (0, 0, 0)
# white = (255, 255, 255)

# # Création de la fenêtre Pygame
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Importer/Télécharger un fichier JSON")

# # Fonction pour ouvrir la fenêtre native de Windows pour sélectionner un fichier
# def open_file_dialog():
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
#     print(file_path,type(file_path))
#     root.destroy()

# # Boucle principale
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False
#         elif event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
#             elif event.key == K_o:
#                 open_file_dialog()

#     # Effacement de l'écran
#     window.fill(white)

#     # Affichage du texte
#     font = pygame.font.SysFont(None, 24)
#     text = font.render("Appuyez sur 'O' pour ouvrir un fichier JSON", True, black)
#     text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
#     window.blit(text, text_rect)

#     # Mise à jour de l'affichage
#     pygame.display.flip()

# # Fermeture de Pygame
# pygame.quit()


import json,os
with open("test.json","r",encoding="utf-8") as f:
    print(type(json.load(f)))