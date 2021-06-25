conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2) #une os elementos dos conjuntos
print('Conjunto 1: {}'.format(conjunto))
print('Conjunto 2: {}'.format(conjunto2))
print('União de conjuntos: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2) #analisa o elemento que se repete em ambos os conjuntos
print ('Intersecção de conjuntos: {}'.format(conjunto_interseccao))

conjunto_diferenca = conjunto.difference(conjunto2) #analisa valores diferentes em ambos os conjuntos
print ('Diferença entre conjuntos: {}'.format(conjunto_diferenca))

conjunto_diff_simetrico = conjunto.symmetric_difference(conjunto2)#analisa os valores que não se repetem entre os conjuntos
print('Diferença simétrica: {}'.format(conjunto_diff_simetrico))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)#analisa se os elementos de determinado conjunto se repetem em outro conjunto, se ele se encontra em outro conjunto
print ('A é subconjunto de B? {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)#analisa se os elementos de um conjunto contém no outro, além dos que ele já possui
print ('B é superconjunto de A? {}'.format(conjunto_superset))

lista = ['cachorro', 'gato', 'elefante', 'gato', 'gato']
conjunto_animais = set(lista)#cria um conjunto da lista e remove automaticamente as duplicidades.
print (conjunto_animais)
lista_animais = list(conjunto_animais)
print (lista_animais)
#conjunto = {1, 2, 3, 4}
#conjunto.add(5) acrescenta elemento
#conjunto.discard(2) remove elemento
#print(conjunto)