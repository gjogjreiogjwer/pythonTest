from firstClass import FirstClass

class SecondClass(FirstClass):
	def __init__(self, value):
		FirstClass.__init__(self, value)
		#super().__init__(value)

	#重写
	def display(self):
		print ('current value = %s' % self.data)

if __name__ == '__main__':
	b = SecondClass(4)
	b.display()