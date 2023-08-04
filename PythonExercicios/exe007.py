'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 007
   NOME: Carlos Henrique
   ENUNCIADO: 007 – Desenvolva um programa que leia as duas notas de um aluno,
   calcule e mostre a sua média.
-----------------------------------------------------------------------------'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('1ºBimestre {:.1f} | 2ºBimestre {:.1f} \nMédia do Aluno {:.1f}'.format(n1, n2, m))
