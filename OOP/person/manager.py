from person import Person

class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mgr', pay)

	def giveRaise(self, percent, bonus=0.1):
		Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
	tom = Manager('Tom Jones', 50000)
	tom.giveRaise(.10)
	print (tom)