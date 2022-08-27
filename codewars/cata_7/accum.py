def accum(s):
    result = ''
    count = 1
    for let in s:
        result += let.upper()
        if count > 1:
            result += let.lower() * (count - 1)
        if count != len(s):
            result += '-'
        count += 1
    return result

def best_decision(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

if __name__ == '__main__':
    assert accum('abc') == 'A-Bb-Ccc', print(accum('abc'))
