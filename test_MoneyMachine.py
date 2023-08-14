import unittest
from money_machine import MoneyMachine


class TestMoneyMachine(unittest.TestCase):
    def setUp(self):
        self.money_machine = MoneyMachine()

    def test_report(self):
        self.money_machine.report()

    def test_make_payment(self):
        self.money_machine.make_payment(2.5)


if __name__ == "__main__":
    unittest.main()
