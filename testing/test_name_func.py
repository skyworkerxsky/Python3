import unittest
from name_func import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    if __name__ == "__main__":
        unittest.main()

    def test_first_last_name(self):
        first = "foo"
        last = "bar"
        result = f"{first} {last}".title()
        formatted_name = get_formatted_name(first, last)
        self.assertEqual(formatted_name, result)

    def test_first_middle_last_name(self):
        first = "foo"
        middle = "bar"
        last = "baz"
        result = f"{first} {middle} {last}".title()
        formatted_name = get_formatted_name(first, last, middle)
        self.assertEqual(formatted_name, result)