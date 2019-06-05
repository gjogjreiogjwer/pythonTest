# -*- coding:utf-8 -*-
# 私有化。

class Student():
	def __init__(self, name):
		#变量名自动扩张，包含所在类的名称
		self.__name = name

	def getName(self):
		return self.__name

if __name__ == '__main__':
	b = Student('dff')
	#print (b.__name)
	#伪私有化
	print (b._Student__name)
	print (b.getName())


