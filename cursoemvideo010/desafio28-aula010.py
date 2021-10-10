#Desafio 28 

from random import randint
from time import sleep

#Computador gerando número aleatório:
pc = randint(0, 5)
print("_____"* 5) #Frufru
print("Estou pensando em um número, você quer adivinhar? ")
print("_____"* 5) #Frufru

#Jogador tentando adivinhar
player = int(input("Em que número estou pensando? "))
print("PROCESSANDO ...")
sleep(3)

if player == pc:
    print("Droga! Você me venceu!")
else: 
    print("Ganhei de você! Pensei no número {}! Quem sabe na próxima!".format(pc))
print("Jogue de novo!")


