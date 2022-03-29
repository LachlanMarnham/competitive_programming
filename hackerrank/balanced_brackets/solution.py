from collections import deque


OPEN_CLOSED_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def is_balanced(string):
    stack = deque()
    OPEN_BRACKETS = OPEN_CLOSED_MAP.keys()

    for char in string:
        # Every time we see an open bracket,
        # add it to the top of the stack
        if char in OPEN_BRACKETS:
            stack.append(char)
        # If we reach a close bracket when
        # there are no items on the stack,
        # we are closing brackets which have
        # not been opened yet
        elif not stack:
            return 'NO'
        # Every time we see a close bracket
        # with a non-empty stack, make sure
        # it is the same species as the item
        # at the top of the stack
        else:
            expected_open = stack.pop()
            expected_close = OPEN_CLOSED_MAP[expected_open]
            if char != expected_close:
                return 'NO'

    # Dangling brackets: if we reach the end of string
    # with characters left on the stack, sting must be
    # un-balanced
    if stack:
        return 'NO'

    return 'YES'
