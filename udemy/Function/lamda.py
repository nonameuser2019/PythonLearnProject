

# example that show using lambda function
square_nums = list(map(lambda x: x * x, range(1, 11)))

# example with filter functions
ages_list = [14, 23, 45, 67, 12, 17, 19, 20, 15]
list_adult = filter(lambda x: x >= 18, ages_list)
print(list_adult)
for age in list_adult:
    print(age)

