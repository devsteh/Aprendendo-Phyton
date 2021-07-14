lista = [1, 10]
arquivo = open('teste.txt', 'r')

try: #tratamento de exceção
    divisao = 10 / 0
    numero = lista[1]
    
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0') 
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimérica') 
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except Exception as ex:
    print('erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando aruivo')
    arquivo.close()