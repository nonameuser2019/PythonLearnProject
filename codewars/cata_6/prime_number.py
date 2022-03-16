import math

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True


assert is_prime(79797979813649) == False
assert is_prime(4) == False
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(73) == True
assert is_prime(75) == False
