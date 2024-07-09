import unittest
from modelo import Calculadora

class CalculadoraTeste (unittest.TestCase):
    def test_verifica_a_eh_numero(self):
        c = Calculadora()
        with self.assertRaises(ValueError):
            c.verifica_numero('a', 5)

    def test_verifica_b_eh_numero(self):
        c = Calculadora()
        with self.assertRaises(ValueError):
            c.verifica_numero(5, 'b')

    def test_verifica_atribuicao(self):
        c = Calculadora()
        self.assertEqual(c.verifica_numero(2, 4), True)
        self.assertEqual(c.a, 2)
        self.assertEqual(c.b, 4)

    def test_adicao_pass(self):
        c = Calculadora()
        r = c.adicao(2, 4)
        self.assertEqual(r, 6)

    def test_adicao_fail(self):
        c = Calculadora()
        r = c.adicao(2, 4)
        self.assertNotEqual(r, 5)

    def test_subtracao_pass(self):
        c = Calculadora()
        r = c.subtracao(2, 4)
        self.assertEqual(r, -2)

    def test_subtracao_fail(self):
        c = Calculadora()
        r = c.subtracao(2, 4)
        self.assertNotEqual(r, 0)

    def test_multiplicacao_pass(self):
        c = Calculadora()
        r = c.multiplicacao(2, 4)
        self.assertEqual(r, 8)

    def test_multiplicacao_fail(self):
        c = Calculadora()
        r = c.multiplicacao(2, 4)
        self.assertNotEqual(r, 9)

    def test_divisao_por_zero(self):
        c = Calculadora()
        with self.assertRaises(ValueError):
            c.divisao(5, 0)

    def test_divisao_pass(self):
        c = Calculadora()
        r = c.divisao(5, 2)
        self.assertEqual(r, 2)

    def test_divisao_fail(self):
        c = Calculadora()
        r = c.divisao(5, 2)
        self.assertNotEqual(r, 10)

if __name__ == '__main__':
    unittest.main()