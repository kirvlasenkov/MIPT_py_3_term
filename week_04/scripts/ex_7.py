import os
from datetime import datetime
from functools import wraps # need to save __name__ and __doc__ 
							# from func to wrapper

from scipy.stats import norm

def logger(filepath):
	"""
	decorator for creating simple logging
	above func with log, located in filepath

	filepath -- path to the log-file
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			time = datetime.now()
			returned_value = func(*args, **kwargs)
			end = datetime.now()
			arguments_unnamed = args
			arguments_named = kwargs

			with open(filepath, "a") as file:
				file.write(
					"Brief information about the call of {}:\n\
					1)begining executing at {}\n\
					2)finishing at {}\n\
					3)returned value by the function {}\n\
					4)list of unnamed values: {}\n\
					5)dictionary of named values: {}\n\
					".format(
						func.__name__,
						time,
						end,
						returned_value if (returned_value is not None) else "-",
						arguments_unnamed, 
						arguments_named
					)
				)
			
			return func(*args, **kwargs)
		return wrapper
	return decorator



if __name__ == "__main__":
	@logger("../log.txt")
	def summary(*args):
		"""
		summarize numbers from args
		"""
		return sum(args)

	@logger("../log.txt")
	def normal_dist_random(
		size: int,
		mean: float,
		std_dev: float) -> list:
		"""
		return random list of variates from Gaussian normal
		distribution

		size -- quantity of elements in variates list
		mean -- value of the mean of distribution
		std_dev -- standard deviation
		"""

		return norm(mean, std_dev).rvs(size)

	print(summary(1, 2, 3, 4))
	print(normal_dist_random(10, 0, 1))
