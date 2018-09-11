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
            print('Você acertou. O número é {}'.format(entrada))
            print('Você tentou os valores: {}'.format(self.valores_testados))
            print('Você tentou os valores: {}'.format(self.index_valor_testado))
            return entrada
        else:
            if entrada > self.numero:
                print("Tente um valor mais baixo!!")
            else:
                print("Tente um valor mais alto!!")
        self.tentativa += 1
        self.escolhe_numero()


if __name__ == "__main__":
    JogoDosNumeros().escolhe_numero()
