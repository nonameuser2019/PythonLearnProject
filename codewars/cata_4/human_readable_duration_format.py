def format_duration(seconds):
    result = ''
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    sec = seconds % 3600 % 60
    if sec > 1:
        result += f'{sec} seconds'
    if sec == 1:
        result += f'{sec} second'

    if minutes > 1:
        if sec:
            result = f'{minutes} minutes and ' + result
        else:
            result = f'{minutes}'
    if minutes == 1:
        if sec:
            result = f'{minutes} minute and ' + result
        else:
            result = f'{minutes} minute'
    if hours > 1:
        if minutes:
            result = f'{hours} hours, ' + result
        else:
            result = f'{hours} hours'
    if hours == 1:
        if minutes:
            result = f'{hours} hour, ' + result
        else:
            result = f'{hours} hour'

    return result


if __name__ == '__main__':
    assert format_duration(1) == '1 second', print(format_duration(1))
    assert format_duration(62) == '1 minute and 2 seconds'
    assert format_duration(3662) == '1 hour, 1 minute and 2 seconds'
