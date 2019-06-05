# -*- coding:utf-8 -*-
# 自定义的异常。

class Bad(Exception):
	pass

def doomed():
	raise Bad()

try:
	doomed()
except Bad:
	print ('got Bad')