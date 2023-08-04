n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2     #soma
m = n1 * n2     #multiplicação
d = n1 / n2     #divisão
di = n1 // n2   #divisão inteira
e = n1 ** n2    #potência (exponenciação)
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e \npotência {}'.format(di, e))
# end='' -> deixa o print de cima e baixo juntos na mesma linha
# \n -> quebra linha no mesmo print (pula linha)