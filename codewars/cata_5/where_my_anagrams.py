import collections

def anagrams(word, words):
    result = []
    example = counter(word)
    for w in words:
       pass


def counter(word):
    c = collections.Counter()
    for letter in word:
        c[letter] += 1
    return c

print(anagrams('hello'))