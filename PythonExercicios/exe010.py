'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 010
   NOME: Carlos Henrique
   ENUNCIADO: 010 – Crie um programa que leia quanto dinheiro uma pessoa tem
   na carteira e mostre quantos Dólares ela pode comprar.
   Considere US$1,00 = R$3,27
-----------------------------------------------------------------------------'''
real = float(input('Quanto tem na carteira? R$'))
dolar= real / 5.21     #cotação referente ao dia que fiz o programa
euro = real / 5.34     #cotação referente ao dia que fiz o programa
iene = real / 0.039    #cotação referente ao dia que fiz o programa
print('Com R${:.2f} você pode comprar US${:.2f} (dólar)!'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f} (euro)!'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥{:.2f} (iene)!'.format(real, iene))
