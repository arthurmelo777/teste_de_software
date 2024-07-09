class Calculadora:
    def __init__(self):
        self._a = 0
        self._b = 0

    @property
    def a (self):
        return self._a
    
    @property
    def b (self):
        return self._b

    def verifica_numero(self, a, b):
        if type(a) is not int:
            raise ValueError("'a' não é um número.")
        if type(b) is not int:
            raise ValueError("'b' não é um número.")

        self.a = a
        self.b = b

        return True

    def adicao(self, a, b):
        if self.verifica_numero(a, b):
            return a + b

    def subtracao(self, a, b):
        if self.verifica_numero(a, b):
            return a - b

    def multiplicacao(self, a, b):
        if self.verifica_numero(a, b):
            return a * b

    def divisao(self, a, b):
        if self.verifica_numero(a, b):
            if (self._b == 0):
                raise ValueError("Divisor deve ser diferente de 0.")
            return a // b