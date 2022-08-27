def solution(args):
    start_interval = str(args[0])
    finish_interval = ''
    for i in range(1, len(args)):
        if args[i] -1 == args[i -1]:
            interval += args[i]


if __name__ == "__main__":
    assert solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) \
           == '-6,-3-1,3-5,7-11,14,15,17-20'