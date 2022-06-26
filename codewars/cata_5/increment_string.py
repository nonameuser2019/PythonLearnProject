import re


def increment_string(strng):
    if not re.findall(r'/d+', strng):
        return strng + '1'
    else:
        num_str = re.findall(r'/d+', strng)
        if num_str[-1] == '9':



if __name__ == '__main__':
    assert increment_string('foo') == 'foo1'
    #assert increment_string('foobar1') == 'foobar2'