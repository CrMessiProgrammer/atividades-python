'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 016
   NOME: Carlos Henrique
   ENUNCIADO: 016 – Crie um programa que leia um número Real qualquer pelo
   teclado e mostre na tela a sua porção Inteira.
   Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
-----------------------------------------------------------------------------'''
import math
num = float(input('Digite um número real: '))
print('O número real {}, na sua porção inteira ficou {} !'.format(num, math.trunc(num)))
