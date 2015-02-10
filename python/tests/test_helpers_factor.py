import unittest
from helpers.factor import prime_factors, num_factors


class HelpersFactorTest(unittest.TestCase):

	def test_prime_factors(self):
		self.assertEqual(prime_factors(28), [2, 2, 7])
		self.assertEqual(prime_factors(4), [2, 2])
		self.assertEqual(prime_factors(36), [2, 2, 3, 3])

	def test_num_factors(self):
		self.assertEqual(num_factors(28), 6)
		self.assertEqual(num_factors(4), 3)
		self.assertEqual(num_factors(36), 9)


if __name__ == "__main__":
	unittest.main()
