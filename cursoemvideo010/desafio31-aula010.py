#DESAFIO 31

#Perguntando a distância da viagem em km:
km = float(input("Qual é a distância da viagem? "))

#Calculando a passagem:
cal1 = km*0.50
cal2 = km*0.45

#Se?
if km <= 200:
    print("Você irá pagar R${:.2f} de passagem!".format(cal1))
else:
    print("Você irá pagar R${:.2f} de passagem!".format(cal2))
print("Boa viagem!")