'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 008
   NOME: Carlos Henrique
   ENUNCIADO: 008 – Escreva um programa que leia um valor em metros e
   o exiba convertido em centímetros e milímetros.
   Bônus: km | hm | dam | dm | cm | mm
-----------------------------------------------------------------------------'''
m = float(input('Digite um valor em metros: '))
km = m / 1001
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m, Corresponde à: '.format(m))
print('{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))
