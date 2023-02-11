class PriorityQueue:
    def __init__(self) -> None:
        self._queue = {}
        self._max_priority = -1

    def add(self, val, priority) -> None:
        if priority not in self._queue:
            self._queue[priority] = []
        self._queue[priority].append(val)
        if priority > self._max_priority:
            self._max_priority = priority

    def pop(self):
        if self._max_priority == -1:
            raise ValueError("Cannot pop from empty queue")
        val = self._queue[self._max_priority].pop(0)
        if not self._queue[self._max_priority]:
            self._queue.pop(self._max_priority)
            if not self._queue:
                self._max_priority = -1
            else:
                self._max_priority = max(self._queue)
        return val


q = PriorityQueue()
q.add("a", 10)
q.add("g", 1)
q.add("f", 2)
q.add("b", 9)
q.add("c", 8)
q.add("d", 8)
q.add("e", 8)

while True:
    print(q.pop())

# expected result abcdefg, followed by exception
