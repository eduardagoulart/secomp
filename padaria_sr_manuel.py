"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""

preco_pao = float(input("Informe o preço do pão: "))
preco_unidade = preco_pao

for quantidade_pao_vendido in range(1, 51):
    preco_pao = round(preco_pao, 2)
    print(f'{quantidade_pao_vendido} - R${preco_pao}')
    preco_pao += preco_unidade

print('---- ' * 10)


# -------------------------------------------- // ------------------------------------------

def padaria(preco_pao):
    preco_unidade = preco_pao
    quantidade_pao_vendido = 0
    while quantidade_pao_vendido != 50:
        quantidade_pao_vendido += 1
        preco_pao = round(preco_pao, 2)
        print(f'{quantidade_pao_vendido} - R${preco_pao}')
        preco_pao += preco_unidade

    return


padaria(preco_unidade)
print("----" * 10)


# -------------------------------------------- // ------------------------------------------

def padaria_recursivo(preco_pao, peco_unidade, quantidade_pao_vendido):
    preco_pao = round(preco_pao, 2)
    print(f'{quantidade_pao_vendido} - {preco_pao}')
    preco_pao += preco_unidade
    quantidade_pao_vendido += 1

    if quantidade_pao_vendido == 51:
        return

    padaria_recursivo(preco_pao, preco_unidade, quantidade_pao_vendido)


preco_pao = preco_unidade
padaria_recursivo(preco_pao, preco_unidade, quantidade_pao_vendido=1)
