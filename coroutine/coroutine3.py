# coding:UTF-8
def producer(consumer_instance):
	"""

	"""
	consumer_instance.send(None)  # 1 use generator.send(None) to activate the generator
	for i in range(5):
		consumer_instance.send(str(i))  # 2 produce something and send to consumer that means send signal to generator
	consumer_instance.close()
	return


def consumer():
	"""
	Consumer is Generator,Not Producer

	"""
	while True:
		number = yield  # 3 get the info from the generator and
		print("The Number Is:{}".format(number))


if __name__ == "__main__":
	producer(consumer())