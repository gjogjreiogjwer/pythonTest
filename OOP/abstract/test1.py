from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
	def delegrate(self):
		self.action()
	@abstractmethod
	def action(self):
		pass

class Sub(Super):
	def action(self):
		print ('ggg')

if __name__ == '__main__':
	b = Sub()
	b.delegrate()
