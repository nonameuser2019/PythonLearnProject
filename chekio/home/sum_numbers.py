import re


def sum_numbers(text):
    list_text = text.split()
    number = sum([int(i) for i in list_text if i.isdigit()])
    return number


assert sum_numbers('hi') == 0
assert sum_numbers('who is 1st here') == 0
assert sum_numbers('my numbers is 2') == 2
assert sum_numbers('This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year') == 3755
assert sum_numbers('5 plus 6 is') == 11
assert sum_numbers('') == 0