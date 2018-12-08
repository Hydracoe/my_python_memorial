def test():
	"""
	一旦使用了x=yield n这种形式，则该协程一定要接收一个参数，否则则默认接受参数为None
	可以使用下面的or完成默认值赋值
	接受参数后还要完成一次循环回到yield处return参数
	它同时具备两个功能，一是暂停并返回函数，二是接收外部send()方法发送过来的值，重新激活函数
	:return:
	"""
	n = 1
	while True:
		n += 1
		x = yield n
		n = x or n


if __name__ == '__main__':
	T = test()
	print(T)
	print(next(T))
	print(T.send(7))
