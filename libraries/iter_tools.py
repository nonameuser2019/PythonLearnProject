from itertools import *
from time import sleep


#https://docs.python.org/3/library/itertools.html
# method count allows takes infinity iterator. First param from and second step
def iter_count():
    for i in count(1, 1):
        print(i)
        sleep(1)
        if i >= 10:
            break


# cycle infinity repeat given iterable data
def iter_cycle():
    s = 'Hello World!'
    result = islice(cycle(s), 0, len(s) * 5)
    return list(result)


# The repeat func Make an iterator that returns object over and over again. The second param is count stop repeating
def iter_repeat():
    # return list of power number 2
    result = list(map(pow, range(1, 11), repeat(2)))
    return result


if __name__ == '__main__':
    print(iter_repeat())

