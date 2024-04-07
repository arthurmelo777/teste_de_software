import unittest
from modelo import Desconto
from unittest.mock import Mock
class DescontoTeste (unittest.TestCase):
    def test_validar_valor_menor_250(self):
        valor = 249.99
        idade = 12
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertFalse(value)

    def test_validar_valor_igual_250(self):
        valor = 250
        idade = 12
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertTrue(value)

    def test_validar_valor_maior_250(self):
        valor = 250.01
        idade = 12
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertTrue(value)

    def test_calcular_idade_negativa(self):
        valor = 250
        idade = -1
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertFalse(value)

    def test_calcular_idade_igual_0(self):
        valor = 250
        idade = 0
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertTrue(value)

    def test_calcular_idade_igual_1(self):
        valor = 250
        idade = 1
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertTrue(value)

    def test_calcular_idade_igual_23(self):
        valor = 250
        idade = 23
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertTrue(value)

    def test_calcular_idade_igual_24(self):
        valor = 250
        idade = 24
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertTrue(value)

    def test_calcular_idade_igual_25(self):
        valor = 250
        idade = 25
        d = Desconto()
        value = d.aplicarDesconto(valor, idade)
        self.assertFalse(value)

# Não testei o desconto pois não é possível recuperar apenas o valor do
# desconto na classe aplicarDesconto cujos testes foram exigidos

if __name__ == '__main__':
    unittest.main()