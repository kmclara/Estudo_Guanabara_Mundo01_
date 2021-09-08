#Desafio 38

#Pedindo ao usuário dois números inteiros:
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

#Verificando qual é maior, menor ou igual:
#MAIOR:
if numero1>numero2: 
    print("O número {} é maior que o valor {}!".format(numero1, numero2))
elif numero2>numero1:
    print("O valor {} é maior que o valor {}!".format(numero2, numero1))
#MENOR:
if numero1<numero2: 
    print("O valor {} é menor que o valor {}!".format(numero1, numero2))
elif numero2<numero1: 
    print("O valor {} é menor que o valor {}!".format(numero2, numero1))
#IGUAL
if numero1 == numero2:
    print("O valor {} e o valor {} são iguais!".format(numero1, numero2))
elif numero2 == numero1:
    print("O valor {} é igual ao valor {}!".format(numero2, numero1))

print("Obrigada por usar nosso programa!")

#Não era necessário as linhas 11 e 16, pois estão 
#dizendo o mesmo que as linhas 9 e 14. 