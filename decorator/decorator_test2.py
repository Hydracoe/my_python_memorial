from functools import wraps


def function_test(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		print("Before function:{}".format(function))
		info = function(*args, **kwargs)
		print("After function:{}".format(function))
		return info
	
	return wrapper


@function_test
def add(a, b):
	return a + b


if __name__ == '__main__':
	print(add(2, 3))
