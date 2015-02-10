import unittest
from helpers.prime import is_prime, primes_range


class HelpersPrimeTest(unittest.TestCase):

	def test_is_prime(self):
		self.assertEqual(is_prime(0), False)
		self.assertEqual(is_prime(1), False)
		self.assertEqual(is_prime(10), False)
		self.assertEqual(is_prime(2), True)
		self.assertEqual(is_prime(17), True)

	def test_primes_range(self):
		self.assertEqual(primes_range(2), [2])
		self.assertEqual(primes_range(3), [2, 3])
		self.assertEqual(primes_range(10), [2, 3, 5, 7])
		self.assertEqual(primes_range(20), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == "__main__":
	unittest.main()
