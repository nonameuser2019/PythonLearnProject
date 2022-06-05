import data as data


class Indexer:
    # __getitem__ method allows to get item from iterable object by index
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print(f'Get item {index}')
        return self.data[index]

# x = Indexer()
# print(x[0])

class Sliscer:
    # __getitem__ this method also allows to get slice form iterable object
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        if isinstance(index, int):
            print(f'Index is integer. Return element by index')
            return self.data[index]
        print(f'Index is element of slice. Return slice')
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value


x = Sliscer()
# print(x[0])
# print(x[0:2])
x[0] = 20
print(x[0])



