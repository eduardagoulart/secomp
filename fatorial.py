valor = int(input("Digite o valor que deseja calcular: "))


def fat(valor):
    fat = 1
    for i in range(2, valor + 1):
        fat *= i

    return f'{valor}! = {fat}'


print(fat(valor))


# -------------------------------------------- // ------------------------------------------

def fat_recursivo(valor):
    if valor == 0:
        return 0
    if valor == 1:
        return 1
    if valor > 1:
        return fat_recursivo(valor - 1) * valor


print(fat_recursivo(valor))


# -------------------------------------------- // ------------------------------------------

fat = 1

for i in range(2, valor + 1):
    fat *= i

print(f'{valor}! = {fat}')

# -------------------------------------------- // ------------------------------------------
