# 正则匹配
import re

def x(word):
	# 匹配连续出现两个或以上相同的字母
	a = re.search("([a-zA-Z])\\1{1,}", word)
	print (a)
	if a:
		print ('lalala')

if __name__ == '__main__':
	x('aa')


