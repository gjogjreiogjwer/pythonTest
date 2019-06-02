class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay

	def getName(self):
		return self.name

	def getPay(self):
		return self.pay

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))

	#打印一个对象会显示对象的__str__方法返回的内容
	def __str__(self):
		return '[Person: %s, %s]' % (self.getName(), self.getPay())

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', 'dev', 100000)
	sue.giveRaise(.1)
	print (sue.pay)
	print (sue)
	print (sue.__class__.__name__)
	for key in sue.__dict__:
		print (key, '=>', sue.__dict__[key])
