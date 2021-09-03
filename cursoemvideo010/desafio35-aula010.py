#DESAFIO 35

#Pedindo ao usuário três retas:
a = float(input("Me diga a primeira reta: "))
b = float(input("Me diga a segunda reta: "))
c = float(input("Me diga a terceira reta: "))

#Cálculo: 
cal1 = (a+b)
cal2 = (b+c)
cal3 = (a+c)

#Se
if cal1 > c and cal2 > a and cal3 > b:
    print("Suas retas podem formar um triângulo!")
else: 
    print("Suas retas não podem formar um triângulo!")
print("Obrigada por usar nosso programa!")