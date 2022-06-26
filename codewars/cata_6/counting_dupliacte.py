def duplicate_count(text):
    count = 0
    duplicate_str = ''
    for let in text.lower():
        if text.lower().count(let) > 1 and let not in duplicate_str:
            count += 1
            duplicate_str += let
    return count


if __name__ == '__main__':
    assert duplicate_count('abcd') == 0
    assert duplicate_count('aabbccd') == 3
    assert duplicate_count('') == 0
    assert duplicate_count('abcdeaB') == 2
    