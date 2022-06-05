def largest_pr_fac(num):
    for i in range(num // 2, 1, -1):
        if num % i == 0:
            return i


if __name__ == '__main__':
    print(largest_pr_fac(13195))