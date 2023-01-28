from typing import List


class SummaryRanges:
    def __init__(self):
        self._values = [False] * 10_000
        self._max_val = -1

    def add_num(self, value: int) -> None:
        self._values[value] = True
        if value > self._max_val:
            self._max_val = value

    def get_intervals(self) -> List[List[int]]:
        intervals = []
        last_val = False
        for i in range(self._max_val + 2):
            next_val = self._values[i]
            if next_val is True:
                if last_val is False:
                    new_interval = [i]
            if next_val is False:
                if last_val is True:
                    new_interval.append(i - 1)
                    intervals.append(new_interval)
            last_val = next_val
        return intervals
