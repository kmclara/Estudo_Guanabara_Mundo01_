#DESAFIO 33

#Pedindo ao usuário 3 números: 
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

#Verificando quem é menor 
menor = a 
if b<a and b<c:
    menor = b 
if c<a and c<b: 
    menor = c 

#Verificando quem é o maior 
maior = a 
if b>a and b>c:
    maior = b 
if c>a and c>b:
    maior = c 
print("O menor valor é {} e o maior valor é {}!".format(menor, maior))


