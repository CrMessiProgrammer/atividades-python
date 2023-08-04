'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 012
   NOME: Carlos Henrique
   ENUNCIADO: 012 – Faça um algoritmo que leia o preço de um produto e
   mostre seu novo preço, com 5% de desconto.
-----------------------------------------------------------------------------'''
vi = float(input('Valor do produto: R$'))
vf = vi - (vi * (5 / 100))                  #(vi * (5 / 100))  =  5% do valor inicial
print('Com os 5% de desconto o preço do produto ficou de R${:.2f}, por R${:.2f}!'.format(vi, vf))
