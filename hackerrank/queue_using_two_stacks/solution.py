class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, x):
        self._queue.append(x)

    def dequeue(self):
        return self._queue.pop(0)

    def print(self):
        return self._queue[0]


def queue_using_two_stacks(queries):
    queue = Queue()
    results = []
    for query in queries:
        if query.startswith("1"):
            _, x = query.split()
            queue.enqueue(int(x))
        elif query.startswith("2"):
            queue.dequeue()
        else:
            result = queue.print()
            results.append(result)
    return results
