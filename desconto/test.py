import unittest
from modelo import Desconto
from unittest.mock import Mock
class DescontoTeste (unittest.TestCase):
    def test_validar_valor_menor_250(self):
        valor = 249
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
        valor = 251
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

        ## self.servico.isEmPosseDaLoja = Mock(return_value = True)

    def test_calcular_desconto_negativo(self):
        valor = 250
        idade = 25
        d = Desconto()
        d._calculaDesconto = Mock()
        d._calculaDesconto = Mock(return_value=-0.1)
        value = d.aplicarDesconto(valor, idade)
        self.assertFalse(value)

if __name__ == '__main__':
    unittest.main()