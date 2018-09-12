numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f'O resultado da soma dos dois números é: {numero1+numero2}')


# -------------------------------------------- // ------------------------------------------


def soma_funcao(numero1, numero2):
    return numero1 + numero2


print(f'O resultado da soma utilizando função é: {soma_funcao(numero1, numero2)}')

# -------------------------------------------- // ------------------------------------------
soma_lambda = lambda valor1, valor2: valor1 + valor2

print(f'O resultado da soma utilizando lambda é: {soma_lambda(numero1, numero2)}')

# -------------------------------------------- // ------------------------------------------
