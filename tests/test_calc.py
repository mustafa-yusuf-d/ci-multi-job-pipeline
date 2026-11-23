import unittest

from app.calc import add, divide, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)




if __name__ == "__main__":
    unittest.main()
