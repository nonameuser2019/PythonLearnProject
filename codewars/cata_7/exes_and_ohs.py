def xo(s):
    return s.lower().count('x') == s.lower().count('o')

if __name__ == "__main__":
    assert xo('xo')
    assert not xo('xoo')
