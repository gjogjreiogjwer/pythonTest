# -*- coding:utf-8 -*-

# 当实例X出现在X[i]这样的索引运算中时，将调用这个实例继承的__getitem__方法。
class Indexer:
	def __init__(self):
		self.data = [5,6,7,8,9]

	def __getitem__(self, index):
		return self.data[index]

# 索引迭代
class Stepper:
	def __init__(self):
		self.data = 'spam'

	def __getitem__(self, index):
		return self.data[index]


if __name__ == '__main__':
	X = Indexer()
	print (X[1])
	print ("***********")
	Y = Stepper()
	for item in Y:
		print (item, end=' ')

