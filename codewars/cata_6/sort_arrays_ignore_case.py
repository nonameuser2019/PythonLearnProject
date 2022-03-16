def sortme(words):
    return sorted(words, key=lambda l: l[:4].lower())

print(sortme(["Hello", "there", "I'm", "fine"]))

