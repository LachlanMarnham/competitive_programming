from datetime import date


def days_diff(a, b):
    date_a = date(*a)
    date_b = date(*b)
    days = (date_a - date_b).days
    return abs(days)
