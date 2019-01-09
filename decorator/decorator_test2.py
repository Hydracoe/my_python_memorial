from functools import wraps


def function_test(functions):
	@wraps(functions)
	def wrapper(*args, **kwargs):
		print("Before function:{}".format(functions))
		info = functions(*args, **kwargs)
		print("After function:{}".format(functions))
		return info
	
	return wrapper


@function_test
def add(a, b):
	return a + b


if __name__ == '__main__':
	print(add(2, 3))
