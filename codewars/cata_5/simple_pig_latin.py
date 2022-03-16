def pig_it(text):
    result = []
    for word in text.split():
        result.append(word[1:] + word[0] + 'ay')
    return ' '.join(result)


def pig_it_2(text: str):
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split()])

print(pig_it_2('Pig latin is cool !'))
assert pig_it_2('Pig latin is cool !') == 'igPay atinlay siay oolcay !'