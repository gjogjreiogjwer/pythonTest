import shelve

db = shelve.open('persondb')
sue = db['Sue Jones']
sue.giveRaise(.10)
print(sue)
db['Sue Jones'] = sue
db.close()