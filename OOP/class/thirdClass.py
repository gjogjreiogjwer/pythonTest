from secondClass import SecondClass

class ThirdClass(SecondClass):
	def __init__(self, value):
		super().__init__(value)

	def __add__(self, other):
		return ThirdClass(self.data + other)

	def __str__(self):
		return '[ThirdClass: %s]' % self.data

	def mul(self, other):
		self.data *= other

if __name__ == '__main__':
	a = ThirdClass('abc')
	a.display()
	#调用__str__
	print (a)
	#调用__add__
	b = a + 'xyz'
	b.display()
	print (b)
	a.mul(3)
	print (a)
