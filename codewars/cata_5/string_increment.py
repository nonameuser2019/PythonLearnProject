#not complited cata
def increment_string(text: str):
    digit = ''
    letter = ''
    for let in text:
        if let.isdigit():
            digit += let
        else:
            letter += let
    return letter + str(int(digit) + 1) if digit else letter + '1'

assert increment_string('foo') == 'foo1'
assert increment_string('foobar001') == 'foobar002'