def get_count(sentence):
    count = 0
    for i in sentence:
        if i in 'aeiou':
            count += 1
    return count


def get_count2(sentence):
    return len([x for x in sentence if x in 'aeiou'])

def get_count3(sentence):
    print(type(x in 'aeiou' for x in sentence))
    return sum(x in 'aeiou' for x in sentence)



if __name__ == '__main__':
    assert get_count('aeiou') == 5, get_count('aeiou')
    assert get_count2('aeiou') == 5, get_count('aeiou')
    print(get_count3('aeiou'))