def capitalize(s):
    result = ['', '']

    for i in range(len(s)):
        if i % 2 == 0:
            result[0] += s[i].upper()
            result[1] += s[i]
        else:
            result[0] += s[i]
            result[1] += s[i].upper()
    return result



assert capitalize("abcdef") == ['AbCdEf', 'aBcDeF']