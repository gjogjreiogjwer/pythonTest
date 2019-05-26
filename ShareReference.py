# -*- coding:utf-8 -*-
# 共享引用

def shareReference1():
	a = 3
	#b成为对象3的一个引用
	b = a
	#a引用了由常量表达式‘spam’所创建的新对象，但是b仍然引用原始对象3
	a = 'spam'
	print(b)

#在一个列表中对一个偏移进行赋值会改变这个列表对象，而不是生成一个新的列表对象。
def shareReference2():
	l1 = [2,3,4]
	l2 = l1
	l1 = 3
	#l1设置成不同的对象，l2仍是引用最初的列表。
	print (l2)
	x1 = [2,3,4]
	x2 = x1
	x1[0] = 9
	#这类修改会覆盖列表对象中的某一部分，这个列表对象与其他对象共享，修改就会影响到l2.
	#避免这种情况发生，使用拷贝（Test4）。
	print (x2)

if __name__ == '__main__':
	shareReference1()
	shareReference2()