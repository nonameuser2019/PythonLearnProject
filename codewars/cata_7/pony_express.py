def riders(stations):
    riders_count = 1
    dist = 0
    if sum(stations) <= 100:
        return 1
    else:
        for st in stations:
            if dist + st <= 100:
                dist += st
            else:
                riders_count += 1
                dist = st
    return riders_count

if __name__ == '__main__':
    assert riders([18, 15]) == 1
    assert riders([43, 23, 40, 13]) == 2
    assert riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]) == 4

