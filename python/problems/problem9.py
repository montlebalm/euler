"""
Question:
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
	For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.

Answer:
	31875000

Resources:
	- http://www.mathsisfun.com/numbers/pythagorean-triples.html
"""

from helpers.timer import print_timing


def a(m, n):
	return (n ** 2) - (m ** 2)


def b(m, n):
	return 2 * m * n


def c(m, n):
	return (n ** 2) + (m ** 2)


@print_timing
def problem9(target):
	m, n = 1, 2
	total = 0

	while total != target:
		# Increment the minute hand if we're over
		if total > target:
			m += 1
			n = m

		# Increment n so we can keep guessing
		n += 1

		total = a(m, n) + b(m, n) + c(m, n)

	return a(m, n) * b(m, n) * c(m, n)


if __name__ == "__main__":
	print(problem9(1000))
