import collections

def anagrams(word, words):
    result = []
    example = sorted(word)
    for w in words:
        if sorted(w) == example:
            result.append(w)
    return result


def anagrams_better(word, words):
    return [w for w in words if sorted(w) == sorted(word)]


print(anagrams_better('abba', ['bbaa', 'acba']))
