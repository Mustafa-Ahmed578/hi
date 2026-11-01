import unittest
from calc import add


class TestCalculator(unittest.TestCase):

    def test_addition_positive_numbers(self):
        self.assertEqual(add(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(add(-5, -3, "+"), -8)


if __name__ == "__main__":
    unittest.main()