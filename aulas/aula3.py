#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))

#if a > b and a > c:
#    print('O maior número é {}'.format(a))
#elif b > a and b > c:
#    print('o maior número é {}'.format(b))
#else:
#    print('o maior número é {}'.format(c))
#print('final do programa')


#Par ou Ímpar
#a = int(input('Digite um valor: '))

#resto = a % 2
#if resto == 0:
#    print('Número par!')
#else:
#    print('Número impar!')

a = int(input('Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print ('Média: {}'.format(media))
else:
    print('Algo de errado não está certo')



