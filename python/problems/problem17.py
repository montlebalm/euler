"""
Question:
	If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
	NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer:
	21124
"""

from helpers.timer import print_timing


unique_map = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
}

tens_map = {
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
}

digits_map = {
	3: "hundred",
	4: "thousand"
}


def get_number_words(num):
	parts = []
	digits = str(num)
	num_digits = len(digits)

	if num_digits > 2:
		# Get the ones indicator for the largest denomination
		# e.g., "one", "two"
		largest_key = int(digits[0])
		parts.append(unique_map[largest_key])

		# Add the quantity indicator
		# e.g., "hundred", "thousand"
		parts.append(digits_map[num_digits])

	# Get the value of the last 2 digits
	tens_value = int(digits[-2:])

	# Make sure we actually have tens digits
	if tens_value > 0:
		if len(parts) > 0:
			parts.append("and")

		if tens_value in unique_map:
			parts.append(unique_map[tens_value])
		else:
			# Get the tens word
			# e.g., "twenty", "thirty"
			tens_key = int(digits[-2] + "0")
			parts.append(tens_map[tens_key])

			# Add the ones digit if it's not 0
			if digits[-1] != "0":
				ones_key = int(digits[-1])
				parts.append(unique_map[ones_key])

	return "".join(parts)


@print_timing
def problem17(upper_limit):
	total_length = 0

	for i in range(1, upper_limit + 1):
		total_length += len(get_number_words(i))

	return total_length


if __name__ == "__main__":
	print(problem17(1000))
