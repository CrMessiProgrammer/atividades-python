'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 005
   NOME: Carlos Henrique
   ENUNCIADO: 005 – Faça um programa que leia um número inteiro e mostre
   na tela o seu sucessor e seu antecessor.
-----------------------------------------------------------------------------'''
n = int(input('Digite um número inteiro: '))
s = n + 1
a = n - 1
print('\nAnalisando o valor {} \nSeu sucessor é {} e o antecessor é {}'.format(n, s, a))
# Outra forma de fazer(não declarando as variáveis ('s') e ('a')  ->>  .format(n, (n+1), (n-1))
