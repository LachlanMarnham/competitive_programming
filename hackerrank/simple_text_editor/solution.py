class Editor:
    def __init__(self):
        self._stack = [""]

    def _add_to_stack(self, s):
        self._stack.append(s)

    def _pop_from_stack(self):
        self._stack.pop()

    @property
    def _current_state(self):
        return self._stack[-1]

    def append(self, w):
        new_state = self._current_state + w
        self._add_to_stack(new_state)

    def delete(self, k):
        new_state = self._current_state[:-k]
        self._add_to_stack(new_state)

    def print(self, k):
        return self._current_state[k - 1]

    def undo(self):
        self._pop_from_stack()
