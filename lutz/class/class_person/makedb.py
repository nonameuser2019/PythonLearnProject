from person import Person, Manager
import shelve


bob = Person('Bob Smith')
sue = Person('Sue Jones', 'Dev', 100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

db = shelve.open('persondb')
for key in db:
    print(f'key{key} => {db[key]}')

