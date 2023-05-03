# # import pygame
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # # Initialisation de Pygame
# # pygame.init()

# # # Configuration de la fenêtre de Pygame
# # size = width, height = 640, 480
# # screen = pygame.display.set_mode(size)

# # # Fonction pour ouvrir la boîte de dialogue de sélection de fichiers
# # def open_file_dialog():
# #     root = Tk()
# #     root.withdraw()
# #     file_path = askopenfilename()
# #     return file_path

# # # Boucle de jeu
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             quit()

# #         # Ouverture de la boîte de dialogue de sélecotion de fichiers lorsque la touche "o" est enfoncée
# #         if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
# #             file_path = open_file_dialog()
# #             print(file_path)

# #     # Mise à jour de l'affichage de Pygame
# #     pygame.display.update()

# import pygame

# pygame.init()

# # Création de la fenêtre
# screen = pygame.display.set_mode((800, 600))

# # Boucle principale
# while True:
#     # Récupération des événements dans la file d'attente
#     for event in pygame.event.get():
#         # Si l'événement est le scroll de la souris
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         if event.type == pygame.MOUSEWHEEL:
#             print(event.y)
#             if event.y > 0: # Si la molette est scrollée vers le haut
#                 print("Molette vers le haut")
#             elif event.y < 0: # Si la molette est scrollée vers le bas
#                 print("Molette vers le bas")

#     # Mise à jour de l'affichage
#     pygame.display.update()


from classes.transition import Transition

a = Transition([1,0.5],[0.15],['in'])

print(a.get_list_of_values())