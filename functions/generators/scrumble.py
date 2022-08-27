# in this module various implementation a small program that shuffle first element to the end of sequence


# implementation with return operator
def scrumble(seq):
    result = []
    for i in range(len(seq)):
        result.append(seq[i:] + seq[:i])
    return result


# implementation with generate result by yield operator
def scrumble2(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


s = 'spam'
# use list comprehension implementation
scr3 = [s[i:] + s[:i] for i in range(len(s))]

# use generator implementation
scr4 = (s[i:] + s[:i] for i in range(len(s)))

scr = scrumble(s)
scr2 = list(scrumble2(s))
print(scr)
print(scr2)
print(scr3)
print(list(scr4))

