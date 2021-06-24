lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'calopsita']
#print(lista_animal[2])

soma = 0
for x in lista:
    print(x)
    soma += x
print (soma)

#print (sum(lista)) -> Faz a soma direto da lista
#print (max(lista)) -> Retorna o maior valor da lista
#print (max(lista_animal)) -> Retorna o maior valor da lista, no caso vai puxar pela ordem o alfabeto qual a posição maior da primeira letra da palavra e puxa a palavra com a posição maior e min para menor

if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista, será incluso')
    lista_animal.append('lobo') #.append inclui novos registros na lista
    print(lista_animal)

lista_animal.pop(1)
print(lista_animal)
#.pop remove um registro da lista, se não inserida a posição, é removida a última posição, como se fosse fila

lista_animal.remove('lobo')
print(lista_animal)
#.remove um registro da lista, se não inserida o nome, é removidao último nome, como se fosse fila

#ordenação de lista 
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

#ordenação de lista reversa
lista_animal.reverse()
print(lista_animal)


