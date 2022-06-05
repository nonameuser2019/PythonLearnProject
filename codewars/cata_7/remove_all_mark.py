class List:

    def remove_(self, integer_list, values_list):
        return [num for num in integer_list if num not in values_list]



if __name__ == '__main__':
    l = List()
    integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
    values_list = [1, 3]
    assert l.remove_(integer_list, values_list) == [2, 2, 4]
