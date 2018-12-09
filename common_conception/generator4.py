def test():
	for i in range(10):
		yield i


def wrapper1(something):
	yield something


def wrapper2(something):
	for ins in something:
		yield ins


if __name__ == '__main__':
	wrapper_instance = wrapper1(test())
	print(next(wrapper_instance))
	wrapper_instance = wrapper2(test())
	print(next(wrapper_instance))
	print(next(wrapper_instance))
