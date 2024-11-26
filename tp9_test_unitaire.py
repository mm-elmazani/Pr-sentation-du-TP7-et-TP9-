from tp7_implémentée import Fraction
import unittest



class TestFraction(unittest.TestCase):

    def test_initialization(self):
        # Test de l'initialisation normale
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)

        # Test avec un dénominateur égal à zéro (doit lever une exception)
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_str_representation(self):
        # Test de la méthode __str__
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_addition(self):
        # Test de l'addition
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.num, 5)
        self.assertEqual(result.den, 6)

    def test_subtraction(self):
        # Test de la soustraction
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        result = f1 - f2
        self.assertEqual(result.num, 1)
        self.assertEqual(result.den, 2)

    def test_multiplication(self):
        # Test de la multiplication
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result.num, 6)
        self.assertEqual(result.den, 12)

    def test_division(self):
        # Test de la division
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 3)
        result = f1 / f2
        self.assertEqual(result.num, 9)
        self.assertEqual(result.den, 8)

        # Test de la division par zéro
        f3 = Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            f1 / f3

    def test_power(self):
        # Test de l'opérateur puissance
        f = Fraction(2, 3)
        result = f ** 2
        self.assertEqual(result.num, 4)
        self.assertEqual(result.den, 9)

        # Test puissance zéro
        result_zero = f ** 0
        self.assertEqual(result_zero.num, 1)
        self.assertEqual(result_zero.den, 1)

        # Test puissance négative
        result_neg = f ** -1
        self.assertEqual(result_neg.num, 3)
        self.assertEqual(result_neg.den, 2)

    def test_comparison(self):
        # Test de l'égalité
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2)

        f3 = Fraction(1, 3)
        self.assertFalse(f1 == f3)

    def test_float_conversion(self):
        # Test de la conversion en float
        f = Fraction(3, 4)
        self.assertEqual(float(f), 0.75)

    def test_properties(self):
        # Test de la propriété is_zero
        f1 = Fraction(0, 1)
        self.assertTrue(f1.is_zero())

        f2 = Fraction(1, 2)
        self.assertFalse(f2.is_zero())

        # Test de la propriété is_integer
        f3 = Fraction(6, 3)
        self.assertTrue(f3.is_integer())

        f4 = Fraction(1, 3)
        self.assertFalse(f4.is_integer())

        # Test de la propriété is_proper
        f5 = Fraction(1, 2)
        self.assertTrue(f5.is_proper())

        f6 = Fraction(5, 3)
        self.assertFalse(f6.is_proper())

        # Test de la propriété is_unit
        f7 = Fraction(1, 2)
        self.assertTrue(f7.is_unit())

        f8 = Fraction(2, 3)
        self.assertFalse(f8.is_unit())

    def test_is_adjacent_to(self):
        # Test de fractions adjacentes
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        f3 = Fraction(1, 6)
        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(f3))

        # Test avec une instance non Fraction
        with self.assertRaises(TypeError):
            f1.is_adjacent_to(0.5)


if __name__ == '__main__':
    unittest.main()
