import argparse
from numpy import sqrt


def n_prime_number(n: int) -> list:
	'''
	Return a list of the prime nums,
	 which contains precisely n elements.
	 Default Eratosthene algo
		
	n -- len of the list
	'''
	prime_list = []
	i = 2
	while len(prime_list) != n:
		for j in prime_list:
			if i % j == 0:
				break
		else:
			prime_list.append(i)

		i+=1

	return prime_list 


if __name__ == "__main__":

	# creating parser
	parser = argparse.ArgumentParser(description="showing prime numbers")
	parser.add_argument(
		'--show-all',
		'-a',
		action="store_true",
		help="showing also all previous \
		prime numbers before N"
	)
	parser.add_argument(
		'--file',
		 '-f',
		 action="store",
		 type=argparse.FileType("w"),
		 help="file for output"
	)
	parser.add_argument(
		'number',
		type=int
	)
	
	namespace = parser.parse_args()
	
	output_line = "the {}(th or st, nd, rd or smth else) prime number is {}".format(
	namespace.number, n_prime_number(namespace.number)[-1])
	if namespace.show_all is None:
		print(output_line)

	if namespace.show_all:
		print("first n prime numbers == {}".format(n_prime_number(namespace.number)))
		if namespace.file:
			print(output_line, file=namespace.file)

	if namespace.file:
		print("Just check my message in {}".format(namespace.file))
		print(output_line, file=namespace.file)



	


