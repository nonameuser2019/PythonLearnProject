def first_non_repeating_letter(string: str):
    result = [l for l in string if string.lower().count(l.lower()) == 1]
    return result[0] if result else ''

assert first_non_repeating_letter('stress') == 't'
assert first_non_repeating_letter('aa') == ''