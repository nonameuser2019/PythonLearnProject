def decode_morse(morse_code):
    code_data = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-,': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
        '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.---': 'J'
    }
    result = ''
    for word in morse_code.split('   '):
        for letter in word.split(' '):
            result += code_data.get(letter, ' ')
        result += ' '
    return result.strip()



if __name__ == '__main__':
    assert decode_morse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE', decode_morse('.... . -.--   .--- ..- -.. .')