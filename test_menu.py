import unittest
from menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_get_items(self):
        items = self.menu.get_items()
        self.assertEqual(items, "latte/espresso/cappuccino/")


if __name__ == "__main__":
    unittest.main()
