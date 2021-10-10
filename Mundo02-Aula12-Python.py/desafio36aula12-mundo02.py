#DESAFIO 36

#Perguntando o salário, valor da casa e quantos anos vai morar na casa: 
salário = float(input("Qual seu salário? "))
casa = float(input("Qual o valor da casa: "))
anos = int(input("Quantos anos pretende morar na casa? "))

#Cálculo prestação mensal e porcentagem do exceder de 30% 
mensal = casa / (anos*12)
print("O valor do aluguel mensal que você terá que pagar é de {:.2f}!".format(mensal))
excedeu = salário * 0.30

#Se? Senão se? Senão?
if mensal > excedeu:
    print("Você não poderá pagar este aluguel! O valor excedeu 30% do seu salário!")
else: 
    print("Você poderá pagar o aluguel! O valor está logo acima!")

print("Obrigada por usar nosso programa!")