# -*- coding:utf-8 -*-
# 写文件。

def writeFile():
	#‘w’才能创建文件
	fr = open('data.txt', 'w')
	fr.write('hello\n')
	fr.write('world\n')
	fr.close()

if __name__ == '__main__':
	writeFile()