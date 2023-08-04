'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 015
   NOME: Carlos Henrique
   ENUNCIADO: 015 – Escreva um programa que pergunte a quantidade de Km
   percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
   Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
-----------------------------------------------------------------------------'''
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (60 * dias) + (0.15 * km)
print('O preço a pagar após {}km percorrido(s) em {} dia(s), é de R${:.2f}!'.format(km, dias, valor))
