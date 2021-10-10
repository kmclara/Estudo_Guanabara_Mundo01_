#Importando mp3 no PYTHON. 

print("import pygame...")
from pygame import mixer 

print("init mixer...")
mixer.init()

print("load `deuseeu.ogg`...")
mixer.music.load("cursoemvideo08/deuseeu.ogg")

print("play mixer...")
mixer.music.play()

input("Agora voce escuta?")