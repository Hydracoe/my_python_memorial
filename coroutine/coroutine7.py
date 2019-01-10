import inspect


def customer():
	while True:
		info = '200 OK'
		receive_message = yield info
		print(receive_message)


def producer(customer_instance):
	print(inspect.getgeneratorstate(customer_instance))
	# customer_instance.send(None)
	next(customer_instance)
	print(inspect.getgeneratorstate(customer_instance))
	receive_message = customer_instance.send("information")
	print(inspect.getgeneratorstate(customer_instance))
	print(receive_message)
	customer_instance.close()
	print(inspect.getgeneratorstate(customer_instance))


if __name__ == '__main__':
	producer(customer())
