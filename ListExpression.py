# -*- coding:utf-8 -*-
# 对矩阵某一列进行操作，一般使用列表表达式。

def listExpression(l):
	res = [row[1] for row in l]
	return res

if __name__ == '__main__':
	print (listExpression([[1,2,3], [4,5,6], [7,8,9]]))