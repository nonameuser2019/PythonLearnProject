def valid_parentheses(string):
    open = '('
    close = ')'
    count = 0
    if string and string[0] == close:
        return False
    for par in string:
        if par == open:
            count += 1
        elif par == close:
            count -= 1
            if count < 0:
                return False
    return True if count == 0 else False


if __name__ == '__main__':
    assert valid_parentheses("hi())(") == False
    assert valid_parentheses('()')
    assert valid_parentheses(')(()))') == False

