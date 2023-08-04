'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 006
   NOME: Carlos Henrique
   ENUNCIADO: 006 – Crie um algoritmo que leia um número e mostre o seu
   dobro, triplo e raiz quadrada.
-----------------------------------------------------------------------------'''
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} valor é {}, \nO triplo é {} e \nA raiz quadrada é {:.2f}'.format(n, d, t, r))
# Outra forma, sem declarar as variáveis 'd', 't' e 'r'   ->>   .format(n, (n*2), (n*3), (n**(1/2))
