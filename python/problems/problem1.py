"""
Question:
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.

Answer:
	233168
"""

from helpers.timer import print_timing


def is_multiple_of(multiples, num):
	for multiple in multiples:
		if num % multiple == 0:
			return True
	return False


@print_timing
def problem1(upper_range, multiples):
	return sum([i for i in range(1, upper_range) if is_multiple_of(multiples, i)])


if __name__ == "__main__":
	print(problem1(1000, [3, 5]))
