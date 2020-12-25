from functools import wraps


def swap(func):
	"""
	decorator, which can reverse
	list of the arguments of function

	func -- decorated function
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
	
		return func(*reversed(args), **kwargs)

	return wrapper

if __name__ == "__main__":
	@swap
	def div(x, y, show=False) -> float:
		"""
		return a result of the division of two numbers

		x, y -- participants of the binary division operation.

		show -- boolean flag, if True - div printing result,
		default: False

		Example:
		dev(x, y) -> x / y 

		"""
		res = x / y
		if show:
			print(res)
		return res

	div(2, 4, show=True)

	
	@swap
	def concatenation(str_1: str, str_2: str) -> str:
		"""
		return result of concatenation of two string types

		str_1 -- the first string
		str_2 -- the second string

		Example:
		concatenation("boom-", "boom") -> "boom-boom"
		concatenation(2, 2) -> AssertionError
		"""
		assert type(str_1) == str and type(str_2) == str,\
		 "Please, enter string-type arguments!"

		return str_1 + str_2


	print(concatenation("Hello,", " World!"))
	# print(concatenation(2, 3))
