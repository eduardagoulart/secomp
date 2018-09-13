eduarda = {'comida_favorita': 'lasanha', 'nascimento': 1997}
# Goulart é um apelido de eduarda
goulart = eduarda
print(goulart is eduarda)
# Identidade
print(id(goulart), id(eduarda))

goulart['altura'] = 1.60

print(eduarda)

isabella = {'comida_favorita': 'lasanha', 'nascimento': 1997, 'altura': 1.60}

print(f'Igualdade: {isabella == eduarda}\n')
print(f'Referência: {isabella is eduarda}')
