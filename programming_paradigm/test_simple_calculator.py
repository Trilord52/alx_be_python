import unittest
from simple_calculator import add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 5), -4)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 3), -3)
        self.assertEqual(multiply(0, 10), 0)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
