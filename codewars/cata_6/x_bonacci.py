def Xbonacci(signature, n):
    x = len(signature)
    for i in range(x, n):
        signature.append(sum(signature[i-x:i]))
    return signature[:n]


assert Xbonacci([0, 1], 10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert Xbonacci([1, 1], 10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]