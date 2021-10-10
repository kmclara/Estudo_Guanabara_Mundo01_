#Estava tentando fazer de  um modo a mão, sem fazer com as funções cos, sin e tan.
#Mas eu resoolvi procurar. 
#Não precisa arrendondar, achei que deveria e taquei a função ceil() 
# e a função trunc(), apaguei, mas era só colocar dentro dos {}
#:.2f... burraaaa, mas aprendi! E encontrei formulas novas. 

#from math import sqrt

#valor = float(input("Digite o valor do angulo:  "))
#valor2 = float(input("Digite o valor de um cateto adj ou oposto: "))

#cos45 = sqrt(2/2)*valor2
#cos30 = sqrt(3/2)*valor2
#cos60 = sqrt(1/2)*valor2

import math 

angulo = float(input("Adicione um angulo: "))
radians = math.radians(angulo)

cos = math.cos(radians)
seno = math.sin(radians)
tang = math.tan(radians)


print("O valor em cosseno, seno e tangente, respectivamente, são {:.2f}, {:.2f}, {:.2f}".format(cos, seno, tang))