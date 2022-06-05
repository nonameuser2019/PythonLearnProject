def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute1(rest):
                res.append(seq[i: i + 1] + x)
        return res


def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute2(rest):
                yield seq[i: i+1] + x


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5]
    per1 = permute1(seq)
    per2 = list(permute2(seq))
    print(per1)
    print(per2)
