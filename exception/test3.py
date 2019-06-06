# -*- coding:utf-8 -*-
# 类异常

class NumErr(Exception):
	pass

class Divzero(NumErr):
	pass

class Oflow(NumErr):
	pass

def func():
	pass


try:
	func()
#捕获numerr和其子类的所有异常，采用这种方法可以在之后添加更多的子类异常
except NumErr:
	pass
