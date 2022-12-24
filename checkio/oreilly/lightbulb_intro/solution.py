from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    BULB_ON = False
    time_switched_on = None
    total_time = 0

    for dt in els:
        if not BULB_ON:
            BULB_ON = True
            time_switched_on = dt
        else:
            BULB_ON = False
            duration = (dt - time_switched_on).total_seconds()
            total_time += duration
    return int(total_time)
