class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == '__main__':
    # for item in Squares(1, 10):
    #     print(item)
    X = Squares(1, 5)
    I = iter(X)
    print(next(I))
    print(next(I))
    print(next(I))
    print(next(I))
    print(next(I))
    print(next(I))


