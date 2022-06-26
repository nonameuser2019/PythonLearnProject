# создать словарь из списка где ключ и значение будет эдемент списка
def to_dict(arr: list) -> dict:
    return dict({key: key for key in arr})

# to sort dict by values

def sort_dict_by_values(dict_data):
    return sorted(dict_data.items(), key=lambda x: x[1])


if __name__ == '__main__':
    dict_data = {1: 'b', 2: 'c', 4: 'd'}
    # print(sort_dict_by_values(dict_data))
    # dict_data = {1: 'b', 2: 'c', 4: 'd'}
    # lst = list(dict_data.items())
    # print(lst)
    # l = [0] * 5
    # print(l)
    result = []
    for key, val in dict_data.items():
        result.append(key)
        result.append(val)
    print(result)

    result = [key for key in dict_data.items()]
    print(result)