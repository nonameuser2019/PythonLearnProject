def society_name(friends):
    return ''.join(sorted([part[0] for part in friends], key=lambda x:x[0]))

if __name__ == '__main__':
    names = ['Alex', 'Fred', 'John', 'Bred']
    print(society_name(names))