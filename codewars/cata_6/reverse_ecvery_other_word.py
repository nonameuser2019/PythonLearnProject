def reverse_alternate(string):
    word_list = string.split()
    result = []
    for word in word_list:
        if word_list.index(word) % 2 != 0:
             result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)

print(reverse_alternate("Did it work?"))
assert reverse_alternate("Did it work?") == "Did ti work?"