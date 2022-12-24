import re


def time_conversion(s):
    pattern = r'^(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d+)(?P<suffix>AM|PM)$'
    result = re.search(pattern, s)
    minutes = result.group('min')
    seconds = result.group('sec')

    hours_int = int(result.group('hour'))
    if result.group('suffix') == 'AM':
        hours_int = hours_int % 12
    else:
        hours_int = hours_int % 12 + 12
    hours = str(hours_int).zfill(2)

    return f'{hours}:{minutes}:{seconds}'
