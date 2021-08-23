#Importando mp3 no PYTHON. 

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("C:\Users\maria\OneDrive\Área de Trabalho\deuseeu.mp3")
pygame.mixer.music.play()
pygame.event.wait()
input()