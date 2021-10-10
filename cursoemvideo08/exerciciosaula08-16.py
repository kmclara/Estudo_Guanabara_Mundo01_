from math import sqrt

cateto1 = float(input("Coloque o valor do cateto oposto: "))
cateto2 = float(input("Coloque o valor do cateto adjacente: "))

#hip = (cateto1**2 + cateto2**2)**(1/2)

#print("O valor da hipotenusa será de {}".format(hip))

#hip = math.hypot(cateto1, cateto2)

#print("O valor da hipotenusa é igual á {:.2f}".format(hip))

hi =  (cateto1**2)+(cateto2**2)

hi2= sqrt(hi)

print("Resultado {}".format(hi2))