string_teste = "essa é uma string que será manipulada"

print('len()')
print(len(string_teste))
print('---- '* 10)

print('upper()')
print(string_teste.upper())
print('---- '* 10)

print('lower()')
print(string_teste.lower())
print('---- '* 10)

print('lower().capitalize()')
print(string_teste.lower().capitalize())
print('---- '* 10)

print('title()')
print(string_teste.title())
print('---- '* 10)

print('split()')
print(string_teste.split())
print('---- '* 10)

print('join()')
print(' some '.join(string_teste.split('a')))
print('ola,'.join(string_teste.split('essa')))
print('---- '* 10)