#DESAFIO 24

city = str(input("Me indique o nome da sua cidade: ")).strip().capitalize()

#indicar se tem o nome santo ou não na cidade:

santo = "Santo" in city

#escrevendo o resultado: 

print("O nome Santo é {} no nome da sua cidade.".format(santo))
