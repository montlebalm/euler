"""
Question:
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.

Answer:
	142913828922
"""

from helpers.timer import print_timing
from helpers.prime import primes_range


@print_timing
def problem10(upper_limit):
	primes = primes_range(upper_limit)
	return sum(primes)


if __name__ == "__main__":
	print(problem10(2000000))
