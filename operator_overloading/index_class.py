class Indexer:
    def __init__(self, data):
        self.arr = data

    def __getitem__(self, index):
        return index

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5]
    ind = Indexer(arr)
    print(ind[1])
