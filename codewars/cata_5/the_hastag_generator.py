def generate_hashtag(s:str):
    result = '#'
    if len(s) == 0 or len(s) > 140:
        return False

    for words in s.split():
        result += words.title().strip()
    return result

def generate_hashtag_2(s: str):
    return '#' + ''.join([w.title().strip() for w in s.split()]) if 0 < len(s) < 140 else False


assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
assert generate_hashtag_2('Codewars Is Nice') == '#CodewarsIsNice'