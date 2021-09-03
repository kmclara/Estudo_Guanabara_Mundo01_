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
print("O menor valor é {}".format(menor))


