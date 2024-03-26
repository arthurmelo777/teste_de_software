import unittest
from modelo import Triangulo

class TrianguloTeste (unittest.TestCase):
    def test_eh_triangulo (self):
        a, b, c = 2, 3, 4
        t = Triangulo(a, b, c)
        self.assertTrue(t.validarForma())

    def test_todos_zeros_ou_menor (self):
        a, b, c = 0, 0, 0
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

        a, b, c = -2, -5, -6
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_a_maior_ou_igual (self):
        a, b, c = 5, 2, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

        a , b, c = 6, 2, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_b_maior_ou_igual (self):
        a, b, c = 2, 5, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

        a, b, c = 2, 6, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_c_maior_ou_igual (self):
        a, b, c = 2, 3, 5
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

        a, b, c = 2, 3, 6
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

class TrianguloTesteEquilatero (unittest.TestCase):
    def test_ehEquilatero (self):
        a, b, c = 2, 2, 2
        t  = Triangulo(a, b, c)
        self.assertTrue(t.ehEquilatero())

    def test_a_diferente_b (self):
        a, b, c = 2, 3, 2
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEquilatero())

    def test_a_diferente_c (self):
        a, b, c = 2, 2, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEquilatero())

    def test_b_diferente_c (self):
        a, b, c = 2, 3, 2
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEquilatero())

class TrianguloTesteIsosceles (unittest.TestCase):
    def test_ehIsosceles (self):
        a, b, c = 2, 2, 3
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehIsosceles())

        a, b, c = 2, 3, 2
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehIsosceles())

        a, b, c = 3, 2, 2
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehIsosceles())

    def test_todos_iguais (self):
        a, b, c = 2, 2, 2
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehIsosceles())

    def test_todos_diferentes (self):
        a, b, c = 2, 3, 4
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehIsosceles())

class TrianguloTesteEscaleno (unittest.TestCase):
    def test_ehEscaleno (self):
        a, b, c = 2, 3, 4
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehEscaleno())

    def test_a_igual_b (self):
        a, b, c = 2, 2, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEscaleno())

    def test_a_igual_c (self):
        a, b, c = 2, 3, 2
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEscaleno())

    def test_b_igual_c (self):
        a, b, c = 3, 2, 2
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEscaleno())


if __name__ == "__main__":
    unittest.main()