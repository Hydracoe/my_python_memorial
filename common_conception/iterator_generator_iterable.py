class Test(object):
	def __init__(self):
		self.number = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		while True:
			self.number += 1
			return self.number


class Test2(object):
	def __init__(self):
		self.number = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		while True:
			self.number += 1
			yield self.number


if __name__ == '__main__':
	test = Test()
	test2 = Test2()
	temp = 0
	for i in test:
		temp += 1
		print(i)
		if temp > 10:
			break
	temp2 = 0
	for i in test2:
		temp2 += 1
		print(i)
		print(next(i))
		if temp2 > 10:
			break
"""
注意：
"""
