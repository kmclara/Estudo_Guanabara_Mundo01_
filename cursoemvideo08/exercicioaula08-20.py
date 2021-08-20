#EXERCICIO 20: O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR 
# A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE 
#LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA. 

from random import shuffle

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

#tbl1 = choice(lista)
#tbl2 = choice(lista)
#tbl3 = choice(lista)
#tbl4 = choice(lista)

#print("O primeiro aluno a apresentar o trabalho é {}".format(tbl1))
#print("O segundo aluno a apresentar o trabalho é {}".format(tbl2))
#print("O terceiro aluno a aprensentar o trabalho é {}".format(tbl3))
#print("O quarto aluno a apresentar o trabalho é {}".format(tbl4))

#Não deveria ter feito neste método com o choice
#Porque a função shurfle é especificamente para embaralhar
#Então poderia ter feito assim:

shuffle(lista)

print("A ordem de apresentação de trabalhos será: ")
print(lista)

#Pro shuffle funcionar, deve-se usar [] e não parenteses
#Por isso na lista usei []