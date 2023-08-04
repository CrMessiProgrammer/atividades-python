'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 019
   NOME: Carlos Henrique
   ENUNCIADO: 019 – O professor quer sortear um dos seus quatro alunos para
   apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
   escrevendo o nome do escolhido.
-----------------------------------------------------------------------------'''
from random import choice
n1 = str(input('Digite o nome do 1ºAluno: '))
n2 = str(input('Digite o nome do 2ºAluno: '))
n3 = str(input('Digite o nome do 3ºAluno: '))
n4 = str(input('Digite o nome do 4ºAluno: '))
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print('O sorteado para apagar o quadro foi o(a): {}.'.format(sorteio))
