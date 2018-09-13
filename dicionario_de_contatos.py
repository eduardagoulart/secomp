"""
Crie um dicionário e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone,endereço.
dados ={“Eduarda”: 20, +5532991542604, R Regina Fazion Cipriane}
"""

dados = {}

while True:
    nome = input("Digite o nome do contato: ")
    idade = int(input("Digite a idade do contato: "))
    telefone = int(input("Digite o telefone do contato: "))
    endereco = input("Digite o endereço do contato: ")
    stop = input("Deseja parar? Y o N")
    stop.lower()
    dados[nome] = idade, telefone, endereco
    if stop == 'y' or stop == 'yes':
        break

print(dados)
