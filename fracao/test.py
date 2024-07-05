import unittest
from modelo import Fracao

class FracaoTest (unittest.TestCase):
    def test_denominador_diferente_de_zero (self):
        f = Fracao(2, 3)
        self.assertEqual(2, f.numerador)
        self.assertEqual(3, f.denominador)

    def test_lanca_erro_denominador_igual_a_zero (self):        
        with self.assertRaises(ValueError):
            f = Fracao(2, 0)

    def test_verifica_reducao_de_fracao (self):
        f = Fracao(2, 4)
        self.assertEqual(1, f.numerador)
        self.assertEqual(2, f.denominador)

if __name__ == '__main__':
    unittest.main()