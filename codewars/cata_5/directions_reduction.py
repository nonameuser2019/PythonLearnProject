def dirReduc(arr):
    result = []
    for i in range(1, len(arr) - 1):
        if arr[i].lower() == 'north' and arr[i + 1].lower() != 'south' and arr[i - 1].lower() != 'south':
            result.append(arr[i])
        if arr[i].lower() == 'south' and arr[i + 1].lower() != 'north' and arr[i - 1].lower() != 'north':
            result.append(arr[i])
        if arr[i].lower() == 'west' and arr[i + 1].lower() != 'east' and arr[i - 1].lower() != 'east':
            result.append(arr[i])
        if arr[i].lower() == 'east' and arr[i + 1].lower() != 'west' and arr[i - 1].lower() != 'west':
            result.append(arr[i])
    return result



if __name__ == '__main__':
    case_1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    assert dirReduc(case_1) == ['WEST']

    case_2 = ["NORTH", "WEST", "SOUTH", "EAST"]
    assert dirReduc(case_2) == ["NORTH", "WEST", "SOUTH", "EAST"]