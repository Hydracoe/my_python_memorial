"""
@asyncio.coroutine与yield from
@asyncio.coroutine：asyncio模块中的装饰器，用于将一个生成器声明为协程。
yield from 其实就是等待另外一个协程的返回。
yield from看成为调用者(caller)和子生成器(sub-generator)之间提供了一种透明地双向通道。这包括了从子生成器中获取数据并向子生成器发送数据。
"""


def test(instance):
	yield from instance


if __name__ == '__main__':
	iter_ins = [1, 3, 5, 7, 9]
	test_instance = test(iter_ins)
	print(next(test_instance))
	print(next(test_instance))
