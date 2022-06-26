def solution(s):
    result = ''
    for let in s:
        if let.islower():
            result += let
        else:
            result += ' ' + let
    return result

# the best solution
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)


if __name__ == '__main__':
    assert solution('helloWorld') == 'hello World', print(solution('helloWorld'))