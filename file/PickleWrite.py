# -*- coding:utf-8 -*-
# pickle模块可以直接在文件中存储几乎任何python对象的高级工具，不需要把字符串转来转去。

class PickleTest:
	def test(self):
		d = {1 : 'a', 2 : 'b'}
		#'wb'表示写入文件,二进制形式
		fr = open('datafile.pkl', 'wb')
		import pickle
		pickle.dump(d, fr)

if __name__ == '__main__':
	b = PickleTest()
	b.test()

