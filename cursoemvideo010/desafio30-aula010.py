#DESAFIO 30

#Perguntando ao usuário um número:
number = int(input("Digite um número: "))

#Se?
if (number%2) == 0:
    print("Seu número é par!")
else:
    print("Seu número é impar!")
print("Adicione outro novamente para ser avaliado!")

#Para saber se um número é par ou impar, basta 
#dividir ele por 2. Se for par, o resto é sempre
#0, não sobra nada. 
#Já se for impar, vai sempre ter resto 1. 