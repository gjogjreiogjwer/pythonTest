import shelve

db = shelve.open('persondb')

print (list(db.keys()))
bob = db['Bob Smith']
print (bob)