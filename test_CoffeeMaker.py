import unittest
from coffee_maker import CoffeeMaker
from menu import MenuItem


class TestCoffeeMaker(unittest.TestCase):
    def setUp(self):
        self.coffee_maker = CoffeeMaker()

    def test_report(self):
        self.coffee_maker.report()

    def test_is_resource_sufficient(self):
        drink = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
        self.assertTrue(self.coffee_maker.is_resource_sufficient(drink))

    def test_make_coffee(self):
        drink = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
        self.coffee_maker.make_coffee(drink)
