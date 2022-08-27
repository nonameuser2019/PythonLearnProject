

# def gen_squares(n):
#     for i in range(n):
#         yield i ** 2
#
# x = gen_squares(2)
# print(next(x))
# print(next(x))
# print(next(x))
#

#-------------------------------------------
# need to get string without spaces and all characters should be capitalize
line = 'aaa bb cc f g k'
new_line = ''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split())))
print(new_line)

numbers = list(filter(lambda x: x > 5, range(10)))
numbers_2 = [x for x in range(10) if x > 5]
print(numbers)
print(numbers_2)

