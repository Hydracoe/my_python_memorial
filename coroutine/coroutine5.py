"""
注意到consumer函数是一个generator，把一个consumer传入produce后：
首先调用c.send(None)启动生成器；
然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
consumer通过yield拿到消息，处理，又通过yield把结果传回(yield右边的变量，如果没有则默认为None)
produce拿到consumer处理的结果，继续生产下一条消息；
produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
最后套用Donald Knuth的一句话总结协程的特点：
“子程序就是协程的一种特例。”
"""
import time


def consumer():
	"""
	注意生产者使用send发送消息 消费者使用yield 接受信息并返回信号给生产者
	:return:
	"""
	r = None  # 信息初始化
	while True:
		# 每次接受的信息为变量n，发送给生产者的信号为r
		n = yield r  # 第一次接受预激信号 发送信息r可以是任意值，且不会被生产者处理
		time.sleep(1)
		if not n:  # 除第一次接受预激信号外，下次接受生产者发送的None,消费者则会处理
			print('--------')
			pass
		else:
			pass
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'


def producer(consumer_instance):
	consumer_instance.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = consumer_instance.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	consumer_instance.close()  # 使用close方法同志消费者结束运行


def producer2(consumer_instance):
	temp = consumer_instance.send(None)
	print(temp)
	n = 0
	while n < 5:
		n = n + 1
		if n == 3:
			n = None
		print('[PRODUCER] Producing %s...' % n)
		if n is None:
			consumer_instance.send(n)
			# consumer_instance.close()
			break
		else:
			r = consumer_instance.send(n)
			print('[PRODUCER] Consumer return: %s' % r)
	consumer_instance.close()


if __name__ == '__main__':
	c = consumer()
	producer2(c)