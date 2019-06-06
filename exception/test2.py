# -*- coding:utf-8 -*-
# 自定义的异常。

class Bad(Exception):
	def __str__(self):
		return 'sorry'

def doomed():
	raise Bad()

try:
	doomed()
except Bad as x:
	# 定制打印显示
	print (x)
	print ('got Bad')