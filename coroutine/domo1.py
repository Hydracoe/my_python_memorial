"""
最简单的协程demo
"""


def simple_coroutine():
	print('-> start')
	while True:
		x = yield
		print('-> receive', x)


if __name__ == '__main__':
	sc1 = simple_coroutine()
	
	next(sc1)
	print('----')
	sc1.send('some_info')
	sc2 = simple_coroutine()
	sc2.send(None)
	print('-----')
	sc2.send('info1')  # 如果直接send而未激活，则 can't send non-None value to a just-started generator
	sc2.send(None)
