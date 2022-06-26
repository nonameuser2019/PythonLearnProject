from functools import reduce

def solve(s):
    max_sub = 0
    sub = 0
    consonants = 'aeiou'
    for let in s:
        if let not in consonants:
            sub += ord(let) - 96
        else:
            if sub > max_sub:
                max_sub = sub
                sub = 0
    return max_sub


if __name__ == '__main__':
    assert solve('zodic') == 26, print(solve('zodic'))

