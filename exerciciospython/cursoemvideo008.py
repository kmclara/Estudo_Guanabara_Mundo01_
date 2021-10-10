#import math

#num = int(input("Digite um número: "))
#raiz = math.sqrt(num)

#print("A raiz de {} é igual á {}!".format(num, math.floor(raiz)))
#print("A raiz de {} é igual á {:.2f}!".format(num, raiz))

from math import sqrt, floor

num = int(input("Adicione um número: "))
raiz = sqrt(num)

print("A raiz de {} é igual á {}!".format(num, floor(raiz)))

