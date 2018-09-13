"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo


Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
"""
saltos = []
for i in range(0, 5):
    distancia = float(input("Digite a distancia do salto: "))
    saltos.append(distancia)

media = 0
for distancia_salto in saltos:
    media += distancia_salto

media = media/5
print(media)
"""


# -------------------------------------------- // ------------------------------------------

def distancia_media():
    return [float(input("Digite a distancia do salto: ")) for i in range(0, 5)]


def soma_lista(lista_saltos):
    return sum(lista_saltos)


def media_saltos(soma_dos_valores):
    return soma_dos_valores / 5


print(media_saltos(soma_lista(distancia_media())))
