import math

class Fracao:
    def __init__(self, a, b):
        if (b == 0):
            raise ValueError('Denominador deve ser diferente de 0.')

        self._numerador, self._denominador = self._reduz_fracao(a, b)

    @property
    def numerador (self):
        return self._numerador

    @property
    def denominador (self):
        return self._denominador

    def _reduz_fracao(self, a, b):
        mdc = math.gcd(a, b)

        return a/mdc, b/mdc