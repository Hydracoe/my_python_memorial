import inspect
import time


def customer():
	while True:
		try:
			info = yield
		except Exception as error:
			print(error)
		else:
			print(info)


def customer2():
	while True:
		try:
			info = yield
		except Exception as error:
			print(error)
		else:
			pass


def customer3():
	while True:
		try:
			info = yield
		except GeneratorExit as error:
			print(error)
		else:
			pass


def customer4():
	while True:
		try:
			info = yield
		except Exception as _:
			raise StopIteration
		else:
			pass


if __name__ == '__main__':
	customer_instance = customer3()
	next(customer_instance)
	customer_instance.throw(GeneratorExit)
	print(inspect.getgeneratorstate(customer_instance))

	print('---------------------------')
	time.sleep(10)
	customer_instance2 = customer2()
	next(customer_instance)
	customer_instance.throw(GeneratorExit)
	print(inspect.getgeneratorstate(customer_instance))

	print('---------------------------')
	time.sleep(10)
	customer_instance3 = customer4()
	next(customer_instance3)
	customer_instance3.throw(Exception)
	print(inspect.getgeneratorstate(customer_instance3))
