# annotation func allows to indicate functions parameters type and return data type.
# also how to see in code below we can see how check that the function return except data type
import math


def counter(array) -> int:
    count = 0
    for i in array:
        count += 1
    return count


data = [1, 2, 3]
assert counter.__annotations__['return'] == int
ann = counter.__annotations__['return']
print(ann)


def pow_func(a: int, b: int) -> float:
    return math.pow(a, b)

pow_func(1.1, 3)
