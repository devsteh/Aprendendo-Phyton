#for + if e else
#a = int(input('Digite um número: '))

#div = 0
#for x in range (1, a+1):
#    resto = a % x
#    print(a, resto)
#    if resto == 0:
#        div += 1

#if div == 2:
#    print('Número {} é primo '.format(a))
#else:
#    print('Número {} não é primo '.format(a))


#######################################
#For dentro de For
#a = int(input('Digite um número: '))
#for num in range(a+1):
#    div = 0
#    for x in range (1, num+1):
#        resto = num % x
#        if resto == 0:
#            div += 1

#    if div == 2:
#        print(num)


#####################################
#Estrutura com while
#nota = int(input('Digite a nota: '))
#while nota > 10:
#    nota = int(input('Nota inválida. Entre com a nota correta: '))

#######################################
#Forçando entradas corretas com while
a = int(input('Nota 1: '))
while a > 10:
    a = int(input('A nota foi digitada incorretamente, digite novamente: '))
b = int(input('Nota 2: '))
while b > 10:
    b = int(input('A nota foi digitada incorretamente, digite novamente: '))
c = int(input('Nota 3: '))
while c > 10:
    c = int(input('A nota foi digitada incorretamente, digite novamente: '))
d = int(input('Nota 4: '))
while d > 10:
    d = int(input('A nota foi digitada incorretamente, digite novamente: '))

media = (a + b + c + d) / 4

if media >= 6:
    print ('Média: {}, você foi passou na matéria!'.format(media))
else:
    print('Média: {}, você foi reprovado.'.format(media))

    