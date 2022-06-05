def spin_words(sentence: str):
    return ''.join(word if len(word) < 5 else word[::-1] for word in sentence.split())




if __name__ == '__main__':
    print(spin_words('Hello'))
    assert spin_words('Hello') == 'olleH'
    assert spin_words('Ok') == 'Ok'
