# -*- coding:utf-8 -*-
# raw字符串抑制转义。如果没有这个，当出现读取'C:\new\text.dat'（出现在windows）时，'\n'会被理解为回车，'\t'会被理解为制表符。
# raw字符串也应用于正则表达式。

def rawString():
	#注意 r
	fr = open(r'/Users/jinyicheng/pythonTest/file/data.txt')
	print (fr.readlines())


if __name__ == '__main__':
	rawString()
