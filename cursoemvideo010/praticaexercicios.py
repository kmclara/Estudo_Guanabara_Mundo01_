#Práticando a teoria. 

#nome = str(input("Diga seu nome: "))

#if nome == "Maria":
   #print("Seu nome é lindo")
#else: 
    #print("Seu nome é feio!")
#print("Boa tarde!")

n1 = float(input("Adicione sua nota: "))
n2 = float(input("Adicione a outra nota: "))

n = (n1+n2)/2

print("A sua média de notas foi de {:.1f}!".format(n))

if n >= 6.0:
    print("Sua média está boa! Parabéns!")
else:
    print("Sua média não está boa! Estude mais na próxima!")
    