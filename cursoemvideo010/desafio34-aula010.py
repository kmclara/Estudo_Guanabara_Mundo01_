#Desafio 34 

#Perguntando o salário:
salário = float(input("Digite seu salário para o cálculo do aumento: "))

#Cálculo dos aumentos:
aumento1 = (0.10+1)*salário 
aumento2 = (0.15+1)*salário 

#Se?
if salário >=1250.00:
    print("O valor total do seu aumento é: R${:.2f}!".format(aumento1))
else:
    print("O valor do seu salário total é: R${:.2f}!".format(aumento2))
print("Obrigada por usar nosso programa!")