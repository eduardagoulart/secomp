from random import randint


class JogoDosNumeros:
    def __init__(self):
        self.numero = randint(1, 100)
        self.index_valor_testado = {}
        self.valores_testados = []
        self.tentativa = 0

    def escolhe_numero(self):
        entrada = int(input("Digite um número: "))
        self.valores_testados.append(entrada)
        self.index_valor_testado[self.tentativa] = entrada
        if entrada == self.numero:
            print(f'Você acertou. O número é {entrada}')
            print(f'Você tentou os valores: {self.valores_testados}')
            print(f'Você tentou os valores: {self.index_valor_testado}')
            return entrada
        self.tentativa += 1
        self.escolhe_numero()


if __name__ == "__main__":
    JogoDosNumeros().escolhe_numero()
