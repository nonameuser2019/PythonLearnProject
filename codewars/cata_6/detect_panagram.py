import string

def is_pangram(s):
    for letter in range(ord('a'), ord('z') + 1):
        if chr(letter) not in s.lower():
            return False
    return True


if __name__ == '__main__':
    s = 'The quick, brown fox jumps over the lazy dog!'
    assert is_pangram(s)