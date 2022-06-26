
def scramble(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    for letter in s2:
        if letter not in s2 or s2.count(letter) > s1.count(letter):
            return False
    return True

# best decision on my opinion
# def scramble(s1, s2):
#     return not any(s1.count(char) < s2.count(char) for char in set(s2))

if __name__ == '__main__':
    #assert scramble('katas', 'steak') == False
    #assert scramble('katas', 'steak') == False
    assert scramble('scriptingjava', 'javascript') == True
    assert scramble('data', 'att') == False