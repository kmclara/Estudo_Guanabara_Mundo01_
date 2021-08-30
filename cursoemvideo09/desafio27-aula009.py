#DESAFIO 27 AULA 009

nome = str(input("Qual seu nome completo? ")).strip()

#Primeiro nome:
prim = nome.split()[0]
print("Seu primeiro nome é {}".format(prim))

#Ultimo nome:
ult = nome.split()[len(nome.split())-1]
print("A ultima palavra do seu nome é {}".format(ult))


