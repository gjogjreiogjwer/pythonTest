# -*- coding:utf-8 -*-
# 如果lambda或者def在函数的定义嵌套在一个循环中，并且引用了上层作用域的变量，
# 该变量被循环所改变，所有在这个循环中产生的函数将会有相同的值--在最后一次循环中引用变量的值。

def makeActions1():
	act = []
	for i in range(5):
		#嵌套作用域中的变量在嵌套的函数被调用时才进行查找，所以它们实际上记住的是同样的值
		#（在最后一次循环迭代中循环变量的值）。在这里i一直等于4.
		act.append(lambda x: i ** x)
	return act

def makeAction2():
	act = []
	for i in range(5):
		#使用默认参数把当前的值传递给嵌套作用域的变量。因为默认参数是在潜逃函数创建时评估的，
		#而不是在其稍后调用中。
		act.append(lambda x, i=i: i ** x)
	return act

if __name__ == '__main__':
	acts1 = makeActions1()
	print (acts1[0](2))
	print (acts1[2](2))
	print (acts1[4](2))
	print ('************')
	acts2 = makeAction2()
	print (acts2[0](2))
	print (acts2[2](2))
	print (acts2[4](2))

