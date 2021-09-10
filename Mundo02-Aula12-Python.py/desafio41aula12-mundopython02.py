#Desafio 41

#Importando datetime
from datetime import date
dataComputador = date.today().year

#Perguntando ao usuário seu ano de nascimento: 
dataNascimento = int(input("Informe sua data de nascimento: "))

#Cálculo para saber a idade do atleta:
idadeAtleta = (dataComputador - dataNascimento)
print("Sua idade é {}. De acordo com ela, sua categoria está logo abaixo!".format(idadeAtleta))

#Se, se senão, senão?
if idadeAtleta <=9:
    print("Sua categoria é a MIRIM! Bons jogos!")
elif idadeAtleta >=10 and idadeAtleta <=14:
    print("Sua categoria é INFANTIL! Bons jogos!")
elif idadeAtleta >=15 and idadeAtleta <=19:
    print("Sua categoria é JUNIOR! Bons jogos!")
elif idadeAtleta == 20:
    print("Sua categoria é SÊNIOR! Bons jogos!")
else:
    print("Sua categoria é MASTER! Bons jogos!")

print("Obrigada por usar nosso programa!")