# coding:UTF-8
def producer():
	for i in range(10):
		yield i


def consumer(producers):
	print(producers)


if __name__ == '__main__':
	consumer(producer())