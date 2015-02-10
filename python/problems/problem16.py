"""
Question:
	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 2^1000?

Answer:
	1366
"""

from helpers.timer import print_timing


@print_timing
def problem16(base, exponent):
	product = base ** exponent
	digits = list(str(product))
	return sum(map(int, digits))


if __name__ == "__main__":
	print(problem16(2, 1000))
