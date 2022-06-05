def make_readable(seconds):
    if (seconds // 3600) < 10:
        hours = f'0{seconds // 3600}'
    else:
        hours = f'{seconds // 3600}'
    if ((seconds % 3600) // 60) < 10:
        minutes = f'0{(seconds % 3600) // 60}'
    else:
        minutes = f'{(seconds % 3600) // 60}'
    if (seconds - int(hours) * 3600 - int(minutes) * 60 < 10):
        sec = f'0{seconds - int(hours) * 3600 - int(minutes) * 60}'
    else:
        sec = seconds - int(hours) * 3600 - int(minutes) * 60
    return f'{hours}:{minutes}:{sec}'

def make_readable_best(seconds):
    return "{0:02d}:{1:02d}:{2:02d}".format(seconds / 3600, seconds / 60 % 60, seconds % 60)


if __name__ == '__main__':
    print(make_readable(60))
    assert make_readable(0) == "00:00:00"
    assert make_readable(5) == "00:00:05"
    assert make_readable(60) == "00:01:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(359999) == "99:59:59"

