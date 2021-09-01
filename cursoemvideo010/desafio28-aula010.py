#Desafio 28 

import random 

print(random.randint(0, 5))

what = float(input("Qual o número escolhido? "))

if what <= 5: 
    print("Parabéns! Você acertou!")
else: 
    print("Sua resposta está errada! Tente novamente!")
print("Obrigada por jogar!")


