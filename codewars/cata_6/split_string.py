
def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i-1]+s[i] for i in range(1, len(s), 2)]

assert solution('asdfadsf') == ['as', 'df', 'ad', 'sf']
assert solution('asdfadsf1') == ['as', 'df', 'ad', 'sf', '1_']
assert solution('') == []