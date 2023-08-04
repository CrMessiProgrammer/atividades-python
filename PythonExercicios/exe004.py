'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 004
   NOME: Carlos Henrique
   ENUNCIADO: 004 – Faça um programa que leia algo pelo teclado e mostre
   na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
-----------------------------------------------------------------------------'''
a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('{} - Só tem espaços? '.format(a), a.isspace())
print('{} - É um número? '.format(a), a.isnumeric())
print('{} - É alfabético? '.format(a), a.isalpha())
print('{} - É alfanumérico? '.format(a), a.isalnum())
print('{} - Está em maiúsculas? '.format(a), a.isupper())
print('{} - Está em minúsculas? '.format(a), a.islower())
print('{} - Está capitalizada? '.format(a), a.istitle())
