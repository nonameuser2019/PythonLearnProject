def first_decision(value: int):
    num = 0
    for i in str(value):
        num += int(i) ** len(str(value))
    return True if num == value else False


def second_decision(value: int):
    num = sum([int(i) ** len(str(value)) for i in str(value)])
    return True if num == value else False


def third_decision(value):
    num = sum(map(lambda n: int(n) ** len(str(value)), str(value)))
    return True if num == value else False


assert first_decision(371) == True
assert first_decision(7) == True
assert first_decision(1634) == True

assert second_decision(371) == True
assert second_decision(7) == True
assert second_decision(1634) == True

assert third_decision(371) == True
assert third_decision(7) == True
assert third_decision(1634) == True