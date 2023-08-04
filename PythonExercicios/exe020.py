'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 020
   NOME: Carlos Henrique
   ENUNCIADO: 020 – O mesmo professor do desafio anterior quer sortear a ordem
   de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
   dos quatro alunos e mostre a ordem sorteada.
-----------------------------------------------------------------------------'''
from random import shuffle
n1 = input('Digite o nome do 1ºAluno: ')
n2 = input('Digite o nome do 2ºAluno: ')
n3 = input('Digite o nome do 3ºAluno: ')
n4 = input('Digite o nome do 4ºAluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será...\n{}'.format(lista))
