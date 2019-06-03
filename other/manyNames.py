# -*- coding:utf-8 -*-
# 命名空间

x = 11

def f():
	print (x)

def g():
	x = 22
	print (x)

class C:
	x = 33
	def m(self):
		x =44
		self.x = 55

if __name__ == '__main__':
	print (x)
	f()
	g()
	b = C()
	print (b.x)
	b.m()
	print (b.x)
	print (C.x)
