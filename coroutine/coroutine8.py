import inspect
import time


def customer():
	while True:
		try:
			receive_message = yield
		except Exception as error:
			print('--------\n')
			print(error)
			print('--------\n')
		else:
			print('consumer received:{}'.format(receive_message))


def customer2():
	while True:
		while True:
			receive_message = yield
			print('consumer received:{}'.format(receive_message))


def producer(customer_instance):
	next(customer_instance)
	print('producer send:information1')
	customer_instance.send("information1")
	customer_instance.throw(Exception("This is a private Exception"))
	print(inspect.getgeneratorstate(customer_instance))
	"""
	generator.throw:会让生成器在暂停的yield表达式处抛出指定的异常，如果生成器处理了抛出的异常，代码会向前执行到下一个yield表达式，而产出的值会成为调用generator.throw方法代码的返回值。如果生成器没有处理抛出的异常，异常会向上冒泡，传到调用方的上下文中。
	"""
	customer_instance.close()
	print(inspect.getgeneratorstate(customer_instance))


if __name__ == '__main__':
	producer(customer())
	time.sleep(5)
	print('***********')
	producer(customer2())

"""
generator.close:会让生成器在暂停的yield表达式处抛出GeneratorExit异常。如果生成器没有处理这个异常，或者抛出了StopIteration异常，调用方不会报错，如果收到GeneratorExit异常，生成器一定不能产出值，否则解释器会抛出RuntimeError异常。生成器抛出的异常会向上冒泡，传给调用方。
from collections import namedtuple

Result = namedtuple("Result", "colunt average")
def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count += 1
		average = total / count
	return Result(count, average)


coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(5)
try:
	coro_avg.send(None)
except StopIteration as e:
	result = e.value
	print(result)
"""
