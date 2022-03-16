def spin_words(sentence: str):
    result = []
    for word in sentence.split():
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)


def spin_words_2(sentence: str):
    result = map(lambda word: word[::-1] if len(word) >= 5 else word, sentence.split())
    return ' '.join(result)


def spin_words_3(sentence: str):
    return ' '.join(map(lambda word: word[::-1] if len(word) >= 5 else word, sentence.split()))


assert spin_words('Welcome') == 'emocleW'
assert spin_words_2('Welcome') == 'emocleW'
assert spin_words_3('Welcome') == 'emocleW'
assert spin_words('Hello hi bro') == 'olleH hi bro'
assert spin_words_2('Hello hi bro') == 'olleH hi bro'
assert spin_words_3('Hello hi bro') == 'olleH hi bro'