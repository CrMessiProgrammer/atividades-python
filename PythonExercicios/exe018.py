'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 018
   NOME: Carlos Henrique
   ENUNCIADO: 018 – Faça um programa que leia um ângulo qualquer e mostre
   na tela o valor do seno, cosseno e tangente desse ângulo.
-----------------------------------------------------------------------------'''
from math import sin, cos, tan, radians
ang = int(input('Digite o valor do ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('No ângulo de {}º...'.format(ang))
print('SENO mede {:.2f} -- COSSENO mede {:.2f} -- TANGENTE mede {:.2f} '.format(sen, cos, tan))
