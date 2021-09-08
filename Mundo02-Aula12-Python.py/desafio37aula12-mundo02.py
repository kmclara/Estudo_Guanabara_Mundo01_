#DESAFIO 37

#Perguntando ao usuário um número para a conversão:
num = int(input("Digite um número inteiro: "))

#Pedindo ao usuário que escolha uma opção:
print(""" Digite a opção de conversão:
[1] BINÁRIO
[2] OCTAL 
[3] HEXADECIMAL """)

opção = int(input("Sua opção: "))

#Se, Se senão, Senão?
if opção == 1: 
    print("{} convertido para binário será {}!".format(num, bin(num)[2:]))
elif opção == 2: 
    print("{} convertido para octal será {}!".format(num, oct(num)[2:]))
elif opção == 3: 
    print("{} convertido para hexadecimal é {}!".format(num, hex(num)[2:]))
else: 
    print("Opção invalida. Tente novamente!")

#Final
print("Obrigada por usar nosso programa!")

#Observação: Linhas 16, 18 e 20 foram colocadas [2:] para realizar o fatiamento, pois,
#logo no começo da conversão, na hora de dar o resultado ao usuário, o Python coloca as
#iniciais das bases numericas junto ao resultado da conversão, e não precisamos dessa informação, 
#pois já damos elas como opção do usuário para que ele escolha o método de conversão. 
#Como o fatiamento entende que 2 é na verdade 3, pois ele sempre pula pra frente, coloca-se 2 para 
#que ele entenda que é na verdade do 3 caracter para frente que deve aparecer ao usuário na hora de 
#mostrar o resultado. 
