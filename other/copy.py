# -*- coding:utf-8 -*-
# 避免共享引用的发生，使用拷贝。

def copyList():
	l1 = [1,2,3]
	l2 = l1[:]
	l1[0] = 9
	print (l2)

#拷贝字典或集合
import copy
def copyDict():
	d = {1:'a', 2:'b'}
	#浅拷贝
	b = copy.copy(d)
	#深拷贝
	b = copy.deepcopy(d)
	print (b)

if __name__ == '__main__':
	copyList()
	copyDict()
