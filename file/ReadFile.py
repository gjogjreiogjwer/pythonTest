# -*- coding:utf-8 -*-
# 读文件。   

def readFile():
	# open('data.txt','r'), 'r'是默认值
	with open('data.txt') as fr:
		text = fr.readlines()
		print (text)
		for line in text:
			#rstrip()去掉末尾的回车
			print (line.rstrip())

if __name__ == '__main__':
	readFile()