#DESAFIO 32

#Importando para saber a data do pc:
from datetime import date 

#Perguntando o ano para o usuário: 
ano = int(input("Adicione o ano que deseja! Se quiser analisar o ano atual, digite 1! "))

#Se?
if ano == 1:
    ano = date.today().year 
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("O ano {} é bissexto!".format(ano))
else:
    print("O ano {} não é bissexto!".format(ano))
print("Obrigada por usar nosso programa!")

#!= diferente, não igual. 