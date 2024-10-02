import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10, 0), 10)
        self.assertEqual(self.calc.add(10, -10), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, 5), 0)
        self.assertEqual(self.calc.subtract(-5, -5), -10)
        self.assertEqual(self.calc.subtract(-5, 0), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(10, 1), 10)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(10, 5), 2)

if __name__ == "__main__":
  unittest.main()


# Remember to write additional test methods for subtract, multiply, and divide.