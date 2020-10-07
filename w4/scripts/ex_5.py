from functools import wraps

def count_even(lst: list) -> int:
	"""
	return a number of the even numbers in list

	lst -- list
	"""
	return len(list(filter(lambda x: x%2==0, lst)))


def improved_count_even(count_even):
	@wraps(count_even)   
	def wrapper(lst):
		if count_even(lst) == 0:
			return "There're no even numbers:("
		elif count_even(lst) > 10:
			return "Too many even numbers in the list"
		else:
			return count_even(lst)

	return wrapper


if __name__ == "__main__":
	list_of_nums = list(map(int, input("Just waiting for numbers:\n").split()))

	print("Before using decorator:\n", count_even(list_of_nums))

	@improved_count_even
	def count_even(lst: list) -> list:
		return len(list(filter(lambda x: x%2==0, lst)))

	print("Before using decorator:\n", count_even(list_of_nums))

	

