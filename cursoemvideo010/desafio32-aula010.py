#DESAFIO 32

#Perguntando o ano para o usuário: 
ano = int(input("Adicione o ano que deseja: "))

#Se?
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("O ano {} é bissexto!".format(ano))
else:
    print("O ano {} não é bissexto!".format(ano))
print("Obrigada por usar nosso programa!")

#!= diferente, não igual. 