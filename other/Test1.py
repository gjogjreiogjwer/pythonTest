# -*- coding:utf-8 -*-
# 下面三个函数会生成结果。

def f(x, l=[]):
	for i in range(x):
		l.append(i*i)
	print (l)

if __name__ == '__main__':
	f(2)
	f(3, [3,2,1])
	#注意第三个，它使用了之前内存地址中存储的旧列表，l = [0,1]
	f(3)