import datetime
from typing import Union


class Time(datetime.time):
    def __sub__(self, other):
        if type(self) != type(other):
            message = f'unsupported operand type(s) for -: "{type(self)}" and "{type(other)}"'
            raise NotImplementedError(message)

        hour_1, hour_2 = self.hour, other.hour
        min_1, min_2 = self.minute, other.minute
        return (hour_1 - hour_2) * 60 + (min_1 - min_2)


def sun_angle(time: str) -> Union[int, str]:
    sunrise = Time.fromisoformat("06:00")
    sunset = Time.fromisoformat("18:00")
    degrees_per_minute = 180 / (sunset - sunrise)

    time_of_day = Time.fromisoformat(time)
    if not sunrise <= time_of_day <= sunset:
        return "I don't see the sun!"

    minutes_since_sunrise = time_of_day - sunrise
    return minutes_since_sunrise * degrees_per_minute
