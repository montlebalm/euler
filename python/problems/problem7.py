"""
Question:
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	What is the 10001st prime number?

Answer:
	104743
"""

from helpers.timer import print_timing
from helpers.prime import is_prime


@print_timing
def problem7(target_index):
	index_ctr = 1
	num = 1

	while index_ctr < target_index:
		num += 2

		if is_prime(num):
			index_ctr += 1

	return num


if __name__ == "__main__":
	print(problem7(10001))
