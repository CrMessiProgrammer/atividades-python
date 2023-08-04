'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 014
   NOME: Carlos Henrique
   ENUNCIADO: 014 – Faça um programa que converta uma temperatura
   digitada em ºC e converta para ºF.
-----------------------------------------------------------------------------'''
c = float(input('Digite o valor ºC(Celsius): '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF !'.format(c, f))
