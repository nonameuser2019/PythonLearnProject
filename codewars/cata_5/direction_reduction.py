def dirReduc(arr):
    result = []
    for i in range(len(arr - 1)):
        if arr[i].lower() == 'north' and arr[i + 1].lower() != 'south':
            result.append(arr[i])
        elif arr[i].lower() == 'south' and arr[i + 1].lower() != 'north':
            result.append(arr[i])



if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    assert dirReduc(a) == ['WEST']

