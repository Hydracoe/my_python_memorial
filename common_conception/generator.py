def test():
	"""
	协程，又称微线程，英文名Coroutine，是运行在单线程中的“并发”
	协程相比多线程的一大优势就是省去了多线程之间的切换开销，获得了更高的运行效率。
	Python中的异步IO模块asyncio就是基本的协程模块。
	但是需要注意的是，多线程和协程的区别在于，协程是单一函数的执行！
	程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧
	:return:
	"""
	n = 1
	n += 1
	yield n


if __name__ == '__main__':
	T = test()
	print(T)
	print(next(T))
	try:
		print(next(T))
	except StopIteration as _:
		pass
