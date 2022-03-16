def find_missing_letter(chars):
    for i in range(1, len(chars)):
        if int(ord(chars[i])) != int(ord(chars[i - 1]) + 1):
            return chr(int(ord(chars[i - 1]) + 1))

assert find_missing_letter(['a','b','c','d','f']) == 'e', find_missing_letter(['a','b','c','d','f'])
assert find_missing_letter(['O','Q','R','S']) == 'P'
