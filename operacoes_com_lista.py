lista_exemplo = ['ola', 3, 'gato', 7.8]
print(lista_exemplo)

lista_str = [1, 9, 8, 6.5, 7.2, 7.1, 7.4, 7.9, 3, 2, 1]
lista_str.sort()
print(f'Ordenado em ordem crescente: {lista_str}\n')

lista_str.reverse()
print(f'Ordenado em ordem decrescente: {lista_str}\n')

print(f'count(): {lista_str.count(1)}\n')

print(f'pop(): {lista_str.pop()}\n')

print(f'pop(9): {lista_str.pop(4)}\n')

lista_str.append(8)
print(f'append(): {lista_str}\n')

lista_str.insert(3, 10)
lista_str.insert(1, 'ola')
print(f'insert(): {lista_str}\n')

print(f'concatenação {lista_str+lista_exemplo}\n')

lista_valores = [x for x in range(1, 10)]
print(f'list comprehension: {lista_valores}')
