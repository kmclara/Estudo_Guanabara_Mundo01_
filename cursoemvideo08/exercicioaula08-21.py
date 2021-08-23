#Importando mp3 no PYTHON. 

from pygame import mixer 

mixer.init()
mixer.music.load("deuseeu.mp3")
mixer.music.play()
input("Agora voce escuta?")