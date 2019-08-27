# -*- coding:utf-8 -*-
# 如果在类中定义了__getitem__()方法，
# 那么他的实例对象（假设为P）就可以这样P[key]取值。
# 当实例对象做P[key]运算时，就会调用类中的__getitem__()方法。

class Library:
	def __init__(self):
		self.books = {'title1':'a', 'title2':'b', 'title3':'c'}

	def __getitem__(self, i):
		return self.books[i]

	def __setitem__(self, key, value):
		self.books[key] = value

if __name__ == '__main__':
	a = Library()
	print (a['title2'])
	# 调用__setitem__
	a['title3'] = 'ccc'
	print (a['title3'])