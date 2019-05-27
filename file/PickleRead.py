# -*- coding:utf-8 -*-
# pickle模块可以直接在文件中存储几乎任何python对象的高级工具，不需要把字符串转来转去。

class PickleTest:
	def test(self):
		#'rb'表示读文件，二进制形式
		fr = open('datafile.pkl', 'rb')
		import pickle
		e = pickle.load(fr)
		print (e)

if __name__ == '__main__':
	b = PickleTest()
	b.test()

