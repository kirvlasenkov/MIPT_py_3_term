import argparse
import typing

def fib(n: int) -> int:
	"""
	Return n-number of fibonacci series
	Dynamic programming realization

	n -- number of the needed fibo-member
	"""
	num_1 = 0
	num_2 = 1
	for __ in range(n):
		num_1, num_2 = num_2, num_1 + num_2
	return num_1


def create_parser(command: str) -> 'argparse.ArgumentParser':
	"""
	Create simple argument parser with one positional argument

	command -- name of the flag; support long name with two dash, 
	also one_letter-name with one dash.
	"""
	parser = argparse.ArgumentParser()

	if len(command) > 1:
		parser.add_argument('--' + str(command))

	else:
		parser.add_argument("-" + str(command))

	return parser


if __name__ == "__main__":
	
	parser = create_parser('n')
	namespace = parser.parse_args()

	print(fib(int(namespace.n)))

	

