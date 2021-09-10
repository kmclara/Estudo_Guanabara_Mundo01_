#Desafio 40

#Perguntando ao aluno sobre a média de duas notas:
nota1 = float(input("Qual a sua primeira nota? "))
nota2 = float(input("Qual a sua segunda nota? "))

#Cálculando a média de notas do aluno:
médiaNota = (nota1 + nota2)/2
print("De acordo com suas notas {} e {}, sua média é de {}.".format(nota1, nota2, médiaNota))

#Se, Se senão, senão?
if médiaNota < 5.0:
    print("De acordo com sua média de {}, você foi reprovado por nota abaixo de 5.0. Estude mais!".format(médiaNota))
elif médiaNota>=5 and médiaNota<=6.9:
    print("De acordo com sua média {}, você está de recuperação".format(médiaNota))
elif médiaNota >7.0:
    print("Parabéns! De acordo com sua média de {}, você foi aprovado!".format(médiaNota))

print("Obrigada por usar nosso programa!")