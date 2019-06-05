# -*- coding:utf-8 -*-

class Spam:
	# 类变量
	numInstances = 0

	def __init__(self):
		Spam.numInstances += 1 

	# 静态方法，没有self，用类名调用
	# 使用装饰器，staticmethod内置方法允许通过实例调用
	@staticmethod
	def printNumInstances():
		print ('number of instances created', Spam.numInstances)

if __name__ == '__main__':
	a = Spam()
	b = Spam()
	Spam.printNumInstances()
	# 使用了staticmethod才行
	a.printNumInstances()
	print (a.numInstances)
