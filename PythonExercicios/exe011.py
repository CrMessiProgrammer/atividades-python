'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 011
   NOME: Carlos Henrique
   ENUNCIADO: 011 – Faça um programa que leia a largura e a altura de uma
   parede em metros, calcule a sua área e a quantidade de tinta necessária
   para pintá-la.
   Sabendo que cada litro de tinta, pinta uma área de 2m².
-----------------------------------------------------------------------------'''
l = float(input('Largura da parede (em metros): '))
a = float(input('Altura da parede (em metros): '))
area = a * l
litro = area / 2
print('Sua parede tem a dimensão de {}x{}, e sua área é de {:.3f}m².'.format(l, a, area))
print('Para pintar a parede, será necessário {}l de tinta.'.format(litro))
