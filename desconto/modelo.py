class Desconto:
    def __init__(self, valor, idade):
        self.valor = valor
        self.idade = idade
        self.desconto = 0

    def validarValor(self):
        if (self.valor < 250.00):
            return False
        
        return True

    def calculaDesconto(self):
        if self.idade <= 12:
            self.desconto = 0.15
        elif self.idade <= 18:
            self.desconto = 0.12
        elif self.idade <= 21:
            self.desconto = 0.05
        elif self.idade <= 24:
            self.desconto = 0.03

        return self.desconto

    def aplicarDesconto(self):
        return self.valor * (1-desconto)