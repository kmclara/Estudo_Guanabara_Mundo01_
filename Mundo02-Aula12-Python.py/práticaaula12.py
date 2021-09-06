#Prática mundo 02 aula 12. 

#Perguntando nome ao usuário. 
nome = str(input("Qual é seu nome? "))

#If, elif and else. 
if nome == "Maria": 
    print("Que nome bonito! Parabéns!")
elif nome == "Pedro" or nome == "Camila":
    print("Está quase lá! Seu nome é mediano!")   
else:
    print("Seu nome não é tão bonito assim! Que pena!")

print("Tenha um bom dia!")
