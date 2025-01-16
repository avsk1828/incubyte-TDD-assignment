import unittest
from addnumber import add  

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        # Test for an empty string, should return 0
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        # Test for a single number, should return the number itself
        self.assertEqual(add("1"), 1)

    def test_multiple_numbers(self):
        # Test for multiple numbers separated by commas
        self.assertEqual(add("1,5"), 6)

    def test_newline_between_numbers(self):
        # Test for numbers separated by newlines
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        # Test for a custom delimiter (e.g., ";")
        self.assertEqual(add("//;\n1;2"), 3)

    def test_custom_delimiter_with_newline(self):
        # Test for custom delimiter with newlines
        self.assertEqual(add("//|\n1|2|3"), 6)

    def test_negative_numbers(self):
        # Test for negative numbers, should raise ValueError with correct message
        with self.assertRaises(ValueError) as context:
            add("//;\n1;-2")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

    def test_multiple_negative_numbers(self):
        # Test for multiple negative numbers, should raise ValueError with correct message
        with self.assertRaises(ValueError) as context:
            add("//;\n1;-2;-3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -3")

    def test_large_numbers(self):
        # Test for large numbers, sum should be correct
        self.assertEqual(add("1000,2000,3000"), 6000)

if __name__ == '__main__':
    unittest.main()
