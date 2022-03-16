def get_score(n):
    return sum([i for i in range(1, n+1)]) * 50


assert get_score(1) == 50
assert get_score(2) == 150
assert get_score(3) == 300
assert get_score(4) == 500
assert get_score(5) == 750