def even_fob(max_fob):
    fob = [1, 2]
    sum = 2
    while True:
        new_fab = fob[-2] + fob[-1]
        if new_fab < max_fob:
            fob.append(new_fab)
            if new_fab % 2 == 0:
                sum += new_fab
        else:
            break
    return sum


if __name__ == '__main__':
    print(even_fob(4000000))
