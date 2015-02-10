"""
Question:
	Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
	How many such routes are there through a 20×20 grid?

Answer:
	137846528820
"""

from helpers.timer import print_timing
from math import factorial


@print_timing
def problem15(sides):
	"""
	Finding the number of combinations can be expressed as the factorial of the
	number of sides times two divided by the factorial of sides	then squared

	For sides = 20

		40!
		-------
		20! ^ 2

	"""
	divisor = factorial(sides * 2)
	dividend = factorial(sides) ** 2
	return int(divisor / dividend)


if __name__ == "__main__":
	print(problem15(20))
