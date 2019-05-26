# -*- coding:utf-8 -*-
# 读文件。
def readFile():
	fr = open('data.txt')
	text = fr.readlines()
	print (text)

if __name__ == '__main__':
	readFile()