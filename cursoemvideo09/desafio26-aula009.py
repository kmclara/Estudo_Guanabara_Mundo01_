#DESAFIO 009

frase = str(input("Adicione uma frase: ")).strip().lower()

#Quantas vezes aparece a letra A na frase?

A = frase.count("a")

#Em que posição a letra A aparece pela primeira vez?

prim = frase.find("a")+1

#Em que posição ela aparece a última vez

ult = frase.rfind("a")+1

print("Quantas vezes aparece {}, primeira {}, ultima {}".format(A, prim, ult))

#Apenas algumas coisas que mudei:
#- rfind: não sabia que poderia usar assim, então
#foi uma das coisas que mudei. rfind faz com que 
#comece a busca do lado direito e adicionei +1 
# - usei apenas find no prim, não sabia que ele
#poderia buscar já a primeira posição da str e
#adicionei +1
# - coloquei strip para retirar os espaços indesejados
#que algum usuário pode vir a fazer. e coloquei 
#lower() junto com a variavel frase. 