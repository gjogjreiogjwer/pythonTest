#把对象存储到数据库中

from person import Person
from manager import Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', 'dev', 100000)
tom = Manager('Tom Jones', 50000)

import shelve 
db = shelve.open('persondb')
for object in (bob, sue, tom):
	db[object.getName()] = object
db.close()
