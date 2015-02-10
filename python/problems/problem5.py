"""
Question:
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer:
	232792560
"""

from helpers.timer import print_timing


def lcm(a, b):
	pair_lcm = b

	while pair_lcm % a != 0:
		pair_lcm += b

	return pair_lcm


@print_timing
def problem5(largest_factor):
	numbers = range(2, largest_factor + 1)
	overall_lcm = 1

	for i, num in enumerate(numbers):
		if i + 1 < len(numbers):
			pair_lcm = lcm(num, numbers[i + 1])
			overall_lcm = lcm(pair_lcm, overall_lcm)

	return overall_lcm


if __name__ == "__main__":
	print(problem5(20))
