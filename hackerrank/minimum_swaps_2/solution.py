class LookupList(list):

    def __init__(self, arr):
        self._val_idx_map = {val: idx for idx, val in enumerate(arr)}
        self._swaps = 0
        super().__init__(arr)

    def index(self, item):
        return self._val_idx_map[item]

    @property
    def swaps(self):
        return self._swaps

    def _update_swap_count(self):
        self._swaps += 1

    def _swap_values_in_map(self, val_1, val_2):
        old_1 = self._val_idx_map[val_1]
        old_2 = self._val_idx_map[val_2]
        self._val_idx_map[val_1] = old_2
        self._val_idx_map[val_2] = old_1

    def swap(self, idx_1, idx_2):
        self._update_swap_count()
        val_1 = self[idx_1]
        val_2 = self[idx_2]

        # Swap values in the underlying list
        self[idx_1], self[idx_2] = val_2, val_1

        # Update the map
        self._swap_values_in_map(val_1, val_2)


def minimum_swaps(arr):
    items = LookupList(arr)

    for idx, val in enumerate(items):
        # The value which should be in this spot...
        partner = idx + 1
        # ... and its pre-swap index
        partner_idx = items.index(partner)

        # The value is already in the right spot
        if val == partner:
            continue

        # Otherwise perform the swap and update
        # the tracker
        items.swap(idx, partner_idx)

    return items.swaps
