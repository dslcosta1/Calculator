import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(3, 2), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
        self.assertEqual(self.calc.somar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 2), 3)
        self.assertEqual(self.calc.subtrair(0, 4), -4)
        self.assertEqual(self.calc.subtrair(-3, -2), -1)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 2), 6)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 5), 0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(6, 2), 3)
        self.assertEqual(self.calc.dividir(-6, 3), -2)
        self.assertEqual(self.calc.dividir(5, 2), 2.5)
        self.assertEqual(self.calc.dividir(0, 1), 0)
        self.assertEqual(self.calc.dividir(10, 0), "Erro: Divisão por zero não permitida.")

if __name__ == "__main__":
    unittest.main()