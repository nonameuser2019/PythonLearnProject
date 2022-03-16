def order(text):
    result = []
    for i in range(10):
        for word in text.split():
            if str(i) in word:
                result.append(word)
    return ' '.join(result)


def order_2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


print(order('is2 Thi1s T4est 3a'))
assert order('is2 Thi1s T4est 3a') == 'Thi1s is2 3a T4est'
assert order_2('is2 Thi1s T4est 3a') == 'Thi1s is2 3a T4est'