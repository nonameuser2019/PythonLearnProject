def multiples(m, n):
    return list(n * m for m in range(1, m + 1))

print(multiples(3, 5))