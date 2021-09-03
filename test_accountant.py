import unittest
from accountant import Accountant

class TestAccountant(unittest.TestCase):
	"""Tests for class Accountant"""

	def setUp(self):
		self.acc = Accountant(0) # Balance will be 0 at the start of every test case

	def test_initial_balance(self):
		self.assertEqual(self.acc.balance,0)
		self.acc = Accountant(100)
		self.assertEqual(self.acc.balance,100)

	def test_deposit(self):
		self.acc.deposit(200)
		self.assertEqual(self.acc.balance,200)

	def test_withdrawal(self):
		self.acc.deposit(200)
		self.acc.deposit(300)
		self.acc.withdraw(100)
		self.assertEqual(self.acc.balance,400)

unittest.main()