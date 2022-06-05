from functools import reduce

def beeramid(bonus, price):
    levels = 0
    spend = 0
    for i in range(1, 1000):
        spend += (i ** 2) * price
        if spend <= bonus:
            levels += 1
    return levels

if __name__ == '__main__':
    assert beeramid(9, 2) == 1
    assert beeramid(21, 1.5) == 3
    assert beeramid(1500, 2) == 12
