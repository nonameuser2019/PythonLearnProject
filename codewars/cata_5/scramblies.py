# is not complited
def scramble(s1, s2):
    for i in s2:
        if i.isalpha() and i.islower() and i not in s1:
            return False
    return True


def scramble_2(s1, s2):
    result = [i for i in s2 if i not in s1]
    return False if result else True


assert scramble('katas', 'steak') == False
assert scramble_2('katas', 'steak') == False
assert scramble_2('scriptjava', 'javascript') == True