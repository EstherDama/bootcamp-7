"""Test suite for super_sum."""
from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase): #all methods that have the word test then it shoulld run!!!
	''' Test Case for super sum '''

	def  test_empty_input(self):
		'''Test empty input '''
		self.assertEqual(super_sum(), 0)

	def test_sum_intergers(self):
		'''Test sum of intergers.'''
		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertEqual(super_sum(-1, 1), 0)
		self.assertNotEqual(super_sum(10, 20, 30), 100)

	def test_string_input(self):
		#super_sum("bug", 1, 2, "pig", "corrupt")
		self.assertEqual(super_sum('string'), 0)

	def test_sum_of_items_in_one_list(self):
		'''Test sum of items in a single list
		'''
		self.assertEqual(super_sum([1, 2, 3]), 6)
