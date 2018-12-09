def test():
	"""
	:return:
	"""
	n = 0
	while True:
		if n > 10:
			break
		else:
			yield n
			n += 1


def test2():
	"""
	
	:return:
	"""
	n = 0
	while True:
		if n > 10:
			raise StopIteration
		else:
			yield n
			n += 1


if __name__ == '__main__':
	# for i in test():
	# 	print(i)
	try:
		for i in test2():
			print(i)
	except StopIteration as _:
		pass
