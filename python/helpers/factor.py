from helpers.prime import is_prime
from functools import reduce
from collections import Counter
import operator


_known_prime_factors = {}
_known_num_factors = {}


def prime_factors(num):
	"""
	Get the prime factors for the given number.
	"""
	if num in _known_prime_factors:
		return _known_prime_factors[num]

	primes = []

	if is_prime(num):
		primes.append(num)
	else:
		for i in range(2, num):
			if num % i == 0 and is_prime(i):
				primes.append(i)
				primes += prime_factors(int(num / i))
				break

	# Store off the result for quick retrieval later
	_known_prime_factors[num] = primes

	return primes


def num_factors(num):
	"""
	Find the number of factors in a given number.
	"""
	if num in _known_num_factors:
		return _known_num_factors[num]

	count = 0

	if num < 2:
		count = num
	elif is_prime(num):
		count = 2
	else:
		# Find the number of times each prime factor appears
		factor_count = Counter(prime_factors(num))

		# Given: [3, 3, 5], the product count would be: (2 + 1) * (1 + 1)
		count = reduce(operator.mul, [v + 1 for (k, v) in factor_count.items()])

	# Store off the result for quick retrieval later
	_known_num_factors[num] = count

	return count