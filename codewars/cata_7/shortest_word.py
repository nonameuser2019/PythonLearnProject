def find_short(s):
    return min(len(word) for word in s.split())

if __name__ == "__main__":
    assert find_short("bitcoin take over the world maybe who knows perhaps") == 3