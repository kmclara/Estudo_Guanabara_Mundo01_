#Importando mp3 no PYTHON. 

import pygame

pygame.init()
pygame.mixer.music.load("deuseeu.mp3.mp3")
pygame.mixer.music.play()
pygame.event.wait()