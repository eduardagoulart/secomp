numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print('O resultado da soma dos dois números é: {}'.format(numero1+numero2))


# -------------------------------------------- // ------------------------------------------


def soma_funcao(numero1, numero2):
    return numero1 + numero2


print('O resultado da soma utilizando função é: {}'.format(soma_funcao(numero1, numero2)))

# -------------------------------------------- // ------------------------------------------
soma_lambda = lambda valor1, valor2: valor1 + valor2

print('O resultado da soma utilizando lambda é: {}'.format(soma_lambda(numero1, numero2)))

# -------------------------------------------- // ------------------------------------------
