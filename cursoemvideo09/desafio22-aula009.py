#DESAFIO 22

name = str(input("Me diga seu nome: "))

#dar o nome com todas as letras maiusculas:
upper = name.upper()

#dar o nome com todas as letras minusculas:
lower = name.lower()

#quantas letras ao todo sem considerar espaços:
len1 = len(name.strip())

#quantas letras tem o primeiro nome:
split = (len(name.split() [0]))

print("O resultado é: {}, {}, {}, {}!".format(upper, lower, len1, split))