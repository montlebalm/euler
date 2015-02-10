"""
Question:
	The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
	The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer:
	25164150
"""

from helpers.timer import print_timing


@print_timing
def problem6(upper_limit):
	sum_squares = sum([num ** 2 for num in range(1, upper_limit + 1)])
	squares_sum = sum([num for num in range(1, upper_limit + 1)]) ** 2
	return squares_sum - sum_squares


if __name__ == "__main__":
	print(problem6(100))
