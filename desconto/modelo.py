class Desconto:
    def __init__(self):
        self._valor = 0
        self._idade = 0
        self._desconto = 0

    def _validarValor(self, valor):
        if (valor < 250.00):
            return False
        
        return True

    def _calculaDesconto(self, idade):
        if idade >= 0:
            if idade <= 12:
                self._desconto = 0.15
            elif idade <= 18:
                self._desconto = 0.12
            elif idade <= 21:
                self._desconto = 0.05
            elif idade <= 24:
                self._desconto = 0.03

        return self._desconto

    def _definirDesconto(self, valor, idade):
        return valor * (1 - self._calculaDesconto(idade))


    def aplicarDesconto(self, valor, idade):
        if self._validarValor(valor):
            if self._calculaDesconto(idade):
                return self._definirDesconto(valor, idade)
            
            return False
            
        return False