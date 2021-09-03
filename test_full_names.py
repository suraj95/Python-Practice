import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
	"""Test for names.py"""
	def test_first_last(self):
		full_name = get_full_name('janis','joplin')
		self.assertEqual(full_name,'Janis Joplin')

	def test_middle(self):
		full_name = get_full_name('david','roth','lee')
		self.assertEqual(full_name.split()[1],'Lee')

unittest.main()