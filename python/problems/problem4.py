"""
Question:
	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers.

Answer:
	906609
"""

from helpers.timer import print_timing


def is_palindrome(num):
	digits = str(num)
	return digits == digits[::-1]


@print_timing
def problem4(digits):
	highest_val = int("9" * digits)
	lowest_val = 10 ** (digits - 1)
	p1 = p2 = highest_val
	largest_palindrome = 0

	while p1 >= lowest_val and p2 >= lowest_val:
		p1 -= 1
		product = p1 * p2

		if product > largest_palindrome and is_palindrome(product):
			largest_palindrome = product

		# Reset
		if p1 == lowest_val:
			p2 -= 1
			p1 = 999

	return largest_palindrome


if __name__ == "__main__":
	print(problem4(3))
