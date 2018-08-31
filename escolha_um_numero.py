from random import randint


class NumberGame:
    def __init__(self):
        self.numero = randint(1, 100)
        self.valor_pos = {}
        self.valor = []
        self.tentativa = 0

    def escolhe_recursivo(self):
        entrada = int(input("Digite um número: "))
        self.valor.append(entrada)
        self.valor_pos[self.tentativa] = entrada
        if entrada == self.numero:
            print(f'Você acertou. O número é {entrada}')
            print(f'Você tentou os valores: {self.valor}')
            print(f'Você tentou os valores: {self.valor_pos}')
            return entrada
        self.tentativa += 1
        self.escolhe_recursivo()


if __name__ == "__main__":
    NumberGame().escolhe_recursivo()
