import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    # Test cases for addition
    def test_add(self):
        self.assertEqual(add(10, 5), 15)  # Normal case
        self.assertEqual(add(-1, 1), 0)   # Negative and positive
        self.assertEqual(add(0, 0), 0)    # Zero case
    
    # Test cases for subtraction
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # Normal case
        self.assertEqual(subtract(-1, 1), -2) # Negative case
        self.assertEqual(subtract(0, 0), 0)   # Zero case

    # Test cases for multiplication
    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)  # Normal case
        self.assertEqual(multiply(-1, 1), -1)  # Negative and positive
        self.assertEqual(multiply(0, 10), 0)   # Zero case

    # Test cases for division
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)    # Normal case
        self.assertEqual(divide(-10, 5), -2)  # Negative case
        self.assertEqual(divide(5, 2), 2.5)   # Float division case
        
        # Edge case: Division by zero should raise a ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

# This will allow running the tests directly from the command line
if __name__ == '__main__':
    unittest.main()
