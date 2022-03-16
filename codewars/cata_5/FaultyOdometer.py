def faulty_odometer(n):
    sum = 0
    for i in range(1, n + 1):
        if str(i).find('4') == -1:
            sum += 1
    return sum


def faulty_odometer_2(n):
    return len([i for i in range(1, n + 1) if str(i).find('4') == -1])

def faulty_odometer_3(n):
    return len(list(filter(lambda x: str(x).find('4') == -1, range(1, 165826622))))

print(faulty_odometer_2(1000000))
# assert faulty_odometer(100) == 81
# assert faulty_odometer(15) == 13
# assert faulty_odometer(55) == 40
# assert faulty_odometer(2005) == 1462
#
#
# assert faulty_odometer_2(2005) == 1462