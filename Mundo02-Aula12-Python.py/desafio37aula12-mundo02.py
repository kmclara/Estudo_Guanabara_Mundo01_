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
