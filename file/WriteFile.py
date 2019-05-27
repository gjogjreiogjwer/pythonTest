# -*- coding:utf-8 -*-
# 写文件。
# 写入的一定是字符串。 l=[1,2]  fr.write(str(l))

def writeFile():
	#‘w’才能创建文件
	fr = open('data.txt', 'w')
	fr.write('hello\n')
	fr.write('world\n')
	fr.close()

if __name__ == '__main__':
	writeFile()