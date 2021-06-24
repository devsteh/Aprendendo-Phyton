lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))

#convertendo lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#convertendo tupla em lista para alteração
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica = [0] = 100
print(type(lista_numerica))

#NÃO HÁ A NECESSIDADE DE CONVERTER TUPLA EM LISTA POIS SE ELA FOI CRIADA O SEU INTUITO NÃO É FAZER ALTERAÇÕES