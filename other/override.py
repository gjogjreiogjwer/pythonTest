# 继承 调用重写

class a():
	def x(self):
		self.y()

	def y(self):
		print ('fsd')

class b(a):
	def y(self):
		print ('d')
		# 调用a类的y()
		a.y(self)

if __name__ == '__main__':
	xx = b()
	# 调用b类的y()
	xx.x()
