class Calculadora:
    def __init__(self, n1, n2):
        self.valor_a = n1
        self.valor_b = n2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora (10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
