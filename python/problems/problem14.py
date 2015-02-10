"""
Question:
	The following iterative sequence is defined for the set of positive integers:

		n → n/2 (n is even)
		n → 3n + 1 (n is odd)

	Using the rule above and starting with 13, we generate the following sequence:

		13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
	Which starting number, under one million, produces the longest chain?
	NOTE: Once the chain starts the terms are allowed to go above one million.

Answer:
	837799
"""

from helpers.timer import print_timing


def _next_collatz(n):
	return n // 2 if n % 2 == 0 else (n * 3) + 1


def collatz_length(n, cache={1: 1}):
	if n in cache:
		return cache[n]

	cache[n] = 1 + collatz_length(_next_collatz(n), cache)

	return cache[n]


@print_timing
def problem14(limit):
	longest = (0, 0)

	for i in range(limit // 2, limit):
		length = collatz_length(i)

		if length > longest[1]:
			longest = (i, length)

	return longest[0]

if __name__ == "__main__":
	print(problem14(1000000))
