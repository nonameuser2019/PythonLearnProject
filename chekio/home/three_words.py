def checkio(words: str) -> bool:
    sum_words = 0
    for word in words.split():
        if word.isalpha():
            sum_words += 1
        elif sum_words >= 3:
            return True
        else:
            sum_words = 0
    return True if sum_words >= 3 else False

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
