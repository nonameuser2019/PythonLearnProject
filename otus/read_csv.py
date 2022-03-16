import csv
from csv import DictReader

with open('text.csv', 'r') as f:
    reader = csv.reader(f)

    #get title
    header = next(reader)

    for row in reader:
        print(dict(zip(header, row)))

print('*************')

with open('text.csv', 'r') as f:
    reader = DictReader(f)

    for row in reader:
        print(row)

