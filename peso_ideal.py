"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

sexo = input("Digite seu sexo: m para masculino e f para feminino: ")
h = int(input("Digite sua altura: "))

if sexo == 'm':
    peso = (72.7 * h) - 58
else:
    peso = (62.1 * h) - 44.7

print(peso)


# -------------------------------------------- // ------------------------------------------

def calcula_peso(sexo, h):
    if sexo == 'm':
        return (72.7 * h) - 58
    return (62.1 * h) - 44.7


calcula_peso(sexo, h)
