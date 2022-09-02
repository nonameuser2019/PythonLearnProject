def longest(str1, str2):
    return ''.join(sorted(set(str1 + str2)))


if __name__ == "__main__":
    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
    assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"