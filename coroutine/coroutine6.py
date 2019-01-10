import random


def consumer():
	response_message = None
	tolerance = 0
	count = -1
	while True:
		receive_message = yield response_message
		count += 1
		if receive_message == 'null':
			response_message = '404'
			tolerance += 1
		else:
			response_message = '200'
		if tolerance == 10:
			response_message = '500'
		if count == 0:
			print('pre_activate')
		else:
			print("<{}>--Consumer get:{}".format(count, receive_message))


def producer(consumer_instance):
	consumer_instance.send(None)
	lis = ['apple', 'banana', 'null']
	count = -1
	while True:
		receive_message = consumer_instance.send(lis[random.randint(0, 2)])
		count += 1
		if receive_message == '500':
			print('enough,the last message is:{}'.format(receive_message))
			consumer_instance.close()
			break
		else:
			pass
		if count == 0:
			print('pre_activate_complete')
		else:
			print("<{}>--Producer get:{}".format(count, receive_message))


if __name__ == '__main__':
	producer(consumer())
