'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 013
   NOME: Carlos Henrique
   ENUNCIADO: 013 – Faça um algoritmo que leia o salário de um funcionário
   e mostre seu novo salário, com 15% de aumento.
-----------------------------------------------------------------------------'''
si = float(input('Salário atual: R$'))
sf = si + (si * (15 / 100))
print('Seu salário era de R${:.2f}, após os 15% de aumento, passou a ser R${:.2f}.'.format(si, sf))
