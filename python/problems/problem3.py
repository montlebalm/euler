"""
Question:
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143?

Answer:
	6857
"""

from helpers.timer import print_timing
from helpers.prime import is_prime


@print_timing
def problem3(target_num):
	for num in range(int(target_num ** 0.5) + 1, 2, -1):
		if target_num % num == 0 and is_prime(num):
			return num

	return None


if __name__ == "__main__":
	print(problem3(600851475143))
