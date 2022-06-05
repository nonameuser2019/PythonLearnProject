def domain_name(url):
    try:
        return url[url.index("//") + 2: url.index(".")]
    except ValueError:
        index = url.index(".") + 1
        return url[index: url.index(".", index)]


if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name('http://www.zombie-bites.com') == 'zombie-bites'