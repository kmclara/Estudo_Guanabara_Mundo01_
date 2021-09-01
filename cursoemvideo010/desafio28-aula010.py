#Desafio 28 

from random import randint

what = int(input("Qual o número escolhido? "))

if what <= 5: 
     n = randint(0, 5)
     print("Eu escolhi no numero {}. Parabéns!".format(n))
else: 
    print("Sua resposta está errada! Tente novamente!")
print("Obrigada por jogar!")


