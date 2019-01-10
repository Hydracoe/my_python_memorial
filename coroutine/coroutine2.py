# coding:UTF-8
import time


def producer():
	for i in range(10):
		time.sleep(1)
		yield str(i)


def consumer(producer_ins):
	while True:
		try:
			print("The Number is:{}".format(next(producer_ins)))
		except StopIteration as _:
			break


if __name__ == '__main__':
	consumer(producer())