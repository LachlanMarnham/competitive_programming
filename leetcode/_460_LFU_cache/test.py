from .solution import LFUCache


def test():
    COMMANDS = ["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    INPUTS = [[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
    OUTPUTS = [ None, None, 1, None, -1, 3, None, -1, 3, 4]
    cache = LFUCache(2)
    for idx, command in enumerate(COMMANDS):
        if command == 'put':
            key, value = INPUTS[idx]
            cache.put(key, value)
        elif command == 'get':
            key = INPUTS[idx][0]
            assert cache.get(key) == OUTPUTS[idx]
