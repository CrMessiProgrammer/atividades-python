'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 017
   NOME: Carlos Henrique
   ENUNCIADO: 017 – Faça um programa que leia o comprimento do cateto oposto
   e do cateto adjacente de um triângulo retângulo, calcule e mostre o
   comprimento da hipotenusa.
-----------------------------------------------------------------------------'''
from math import hypot
print('Nas bases de um Triângulo Retângulo, Digite...')
co = float(input('O comprimento do Cateto Oposto: '))
ca = float(input('O comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa desse triângulo retângulo mede {:.2f} !'.format(hi))
