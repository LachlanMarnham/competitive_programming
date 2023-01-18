import re

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def get_datetime_elements(time):
    DATETIME_PATTERN = r"(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})\s(?P<hour>\d{2}):(?P<min>\d{2})"
    matches = re.search(DATETIME_PATTERN, time)
    elements = {key: int(val) for key, val in matches.groupdict().items()}
    elements["month"] = MONTHS[elements["month"] - 1]
    elements["hour_lbl"] = "hour" if elements["hour"] == 1 else "hours"
    elements["min_lbl"] = "minute" if elements["min"] == 1 else "minutes"
    return elements


def date_time(time: str) -> str:
    elements = get_datetime_elements(time)
    template = "{day} {month} {year} year {hour} {hour_lbl} {min} {min_lbl}"
    return template.format(**elements)
