import math


def nb_year(p0, percent, aug, p):
    years = 0
    while p0 <= p:
        p0 += math.floor(p0 / 100 * percent + aug)
        years += 1
    return years


if __name__ == "__main__":
    assert nb_year(1500, 5, 100, 5000) == 15