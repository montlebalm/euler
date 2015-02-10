# Keep track of all the primes we've seen so far
_known_primes = {2: True}


def is_prime(n):
	if n in _known_primes:
		return True
	else:
		if n < 2:
			return False

		if not n & 1:
			return False

		for x in range(3, int(n ** 0.5) + 1, 2):
			if n % x == 0:
				return False

	_known_primes[n] = True

	return True


def primes_range(end):
	"""
	Find all primes less than or equal to <end> using Eratosthenes Sieve.
	"""
	if end < 2:
		return []

	# Get an array of bools that we'll use to toggle primality
	array = [True for _ in range(end)]

	# Start off by removing "0" and "1"
	array[0] = array[1] = False

	for i in range(2, int(end ** 0.5) + 1):
		if array[i]:
			for ctr in range(i * i, end, i):
				array[ctr] = False

	# Make sure the last index is the number itself
	array.append(is_prime(end))

	return [i for (i, val) in enumerate(array) if val]