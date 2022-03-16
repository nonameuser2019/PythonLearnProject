import re
def alphanumeric(password):
    return True if re.findall(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])', password) else False

assert alphanumeric('hello') == False
assert alphanumeric('0PassWrd') == True