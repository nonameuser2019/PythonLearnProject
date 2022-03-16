def alphabet_position(text: str):
    result = []
    for i in text.lower():
        if i.isalpha():
            result.append(str(ord(i) - 96))
    return ' '.join(result)


def alphabet_position_2(text: str):
    return ' '.join([str(ord(i) - 96) for i in text.lower() if i.isalpha()])


assert alphabet_position('The sunset sets at twelve o\' clock.') == '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
assert alphabet_position_2('The sunset sets at twelve o\' clock.') == '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'



