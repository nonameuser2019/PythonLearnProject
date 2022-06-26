def write_file():
    with open('temp.txt', 'w') as f:
        some_text = 'Hello python 3 I really like this langugage'
        for word in some_text.split():
            f.write(word + '\n')

write_file()
for line in open('temp.txt'):
    print(line.strip(), end=' ')
