#EXERCICIO 019 - UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO 
#ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE,
#LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO:

import random 

aluno1 = str(input("Aluno um: "))
aluno2 = str(input("Aluno dois: "))
aluno3 = str(input("Aluno três: "))
aluno4 = str(input("Aluno quatro: "))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(lista)

print("O aluno que irá apagar o quadro é: {}".format(sorteio))

#Tive dificuldade porque não fiz a atividade no mesmo dia e tive que ver um pouco da explicação
#do Gunabara na resolução. Mas tudo bem, me deu uma ideia. 
#posso simplificar no sorteio = rando.choice, colocando from random import choice, que ai ficaria 
# sorteio = choice()