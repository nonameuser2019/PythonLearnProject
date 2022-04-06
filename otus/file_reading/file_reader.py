from csv import DictReader

# with open('file.txt', 'r', newline='') as f:
#     for line in f:
#         print(line)


with open('text.csv', 'r', newline='') as f:
    reader = DictReader(f)

    for row in reader:
        print(row)