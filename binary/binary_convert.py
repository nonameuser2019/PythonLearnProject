def convert_to_dec(bin_num):
    result = 0
    power = 0
    for symbol in str(bin_num)[::-1]:
        result += int(symbol) * 2 ** power
        power += 1
    return result


def convert_to_binary(dec_number):
    bin_num = ''
    while dec_number >= 1:
        bin_num += str(dec_number % 2)
        dec_number //= 2
    return bin_num


num = 99
bin_num = convert_to_binary(num)
print(f'The number: {num} equals {bin_num} in binary')
dec_num = convert_to_dec('0001')
print(f'The binary 0001 equals {dec_num} in decimal')

