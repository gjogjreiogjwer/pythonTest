# -*- coding:utf-8 -*-
# 当try代码块执行时触发异常，跳至except下的代码块，之后会继续运行。

def fetcher(obj, index):
	return obj[index]

x = 'spam'

def catcher1():
	try:
		fetcher(x, 4)
	except IndexError:
		print ('got exception')
	print ('continuing')

def catcher2():
	try:
		# 手动触发异常
		raise IndexError
	except IndexError:
		print ('got excpetion')
	# 有条件触发异常，用于收集约束条件
	# assert False, 'nobody exceptions the spanish'

def catcher3():
	try:
		fetcher(x, 4)
	except IndexError:
		print ('got exception')
	# 没有发生异常时执行
	else:
		print ('no exception')
	#无论是否发生异常，都会执行finally,一般用于关闭文件
	finally:
		print ('after fetch')

if __name__ == '__main__':
	catcher1()
	catcher2()
	catcher3()