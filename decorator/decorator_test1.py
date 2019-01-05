def decorator_function(function):
	def wrapper(*args, **kwargs):
		print("Before function:{}".format(function))
		info = function(*args, **kwargs)
		print("After function:{}".format(function))
		return info
	
	return wrapper


def add(a, b):
	return a + b


@decorator_function
def add2(a, b):
	return a + b


if __name__ == '__main__':
	print(decorator_function(add)(2, 3))
	print(add2(2, 4))
