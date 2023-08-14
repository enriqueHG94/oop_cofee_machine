import unittest
from menu import MenuItem


class TestMenuItem(unittest.TestCase):
    def setUp(self):
        self.menu_item = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)

    def test_name(self):
        self.assertEqual(self.menu_item.name, "latte")

    def test_cost(self):
        self.assertEqual(self.menu_item.cost, 2.5)

    def test_ingredients(self):
        self.assertDictEqual(self.menu_item.ingredients, {"water": 200, "milk": 150, "coffee": 24})
