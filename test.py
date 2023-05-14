import pygame

pygame.init()


print(pygame.Rect([0,5],[5,5]).colliderect(pygame.Rect([0,0],[5,5])))
