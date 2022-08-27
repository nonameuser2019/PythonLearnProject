def strip_comments(strng, markers):
    result = strng
    for m in markers:
        result = result[:result.find(m)] + result[result.find('/n'):]
        print(result)


if  __name__ == "__main__":
    print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
    #assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) ==\
           #'apples, pears\ngrapes\nbananas'