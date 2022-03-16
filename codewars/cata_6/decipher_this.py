# not complited

import re
def decipher_this(string):
    result = []
    for word in string.split():
        if word.isalpha():
            p_1 = re.findall(r'\d+', word)[0]
            word = chr(int(p_1))
            result.append(word)
        else:
            p_1 = re.findall(r'\d+', word)[0]
            p_2 = re.findall(r'[a-zA-Z]+', word)[0][::-1]
            word = chr(int(p_1)) + p_2
            result.append(word)

    print(result)
    return ' '.join(result)

assert decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka") == 'A wise old owl lived in an oak'
