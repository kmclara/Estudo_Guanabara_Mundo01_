#DESAFIO 29

#Perguntando quantos quilomêtros o carro está andando:
question = float(input("Quantos km/hr seu carro está? "))

#Calculo se ele exceder a velocidade: 
km = (question-80)*7

#Se?
if question <= 80:
    print("Você está na velocidade permitida. Prossiga.")
else:
    print("Sua velocidade excedeu! Pague uma multa de R${:.2f}!".format(km))
print("Tenha um ótimo dia! Dirija com segurança!")