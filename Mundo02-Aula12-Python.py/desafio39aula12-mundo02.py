#DESAFIO 39

#Importando o ano do PC:
from datetime import date 

#Perguntando o ano de nascimento do usuário:
nascimento = int(input("Qual o ano do seu nascimento? "))

#Fazendo a função do datetime:
anocomputador = date.today().year

#Cálculo para saber a idade do usuário:
idade = (anocomputador-nascimento)
#Cálculo para mostrar quanto tempo falta ou se passou do ponto:
idadecorreta = 18 
falta = (idadecorreta - idade)
passou = (idade - idadecorreta)

#Se, se senão, senão?
if idade < 18:
    print("Você ainda não precisa se alistar! Falta {} anos".format(falta))
elif idade == 18:
    print("Já é hora de se alistra no exercito militar!")
else: 
    print("Você precisa se alistar! Já se Passou o tempo de alistamento de acordo com sua idade! \n Se passou {} anos!".format(passou))

print("Obrigada por usar nosso programa!")