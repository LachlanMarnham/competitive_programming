def _get_safe_positions(pawns: set) -> set:
    LABEL_COORDINATE_MAP = {}
    COORDINATE_LABEL_MAP = {}

    for f_idx, file in enumerate("abcdefgh"):
        for r_idx, rank in enumerate("12345678"):
            label = file + rank
            coordinate = (f_idx, r_idx)
            LABEL_COORDINATE_MAP[label] = coordinate
            COORDINATE_LABEL_MAP[coordinate] = label

    safe_positions = set()
    for pawn in pawns:
        x, y = LABEL_COORDINATE_MAP[pawn]
        if y < 7:
            if x > 0:
                safe_coordinates = (x - 1, y + 1)
                safe_label = COORDINATE_LABEL_MAP[safe_coordinates]
                safe_positions.add(safe_label)
            if x < 7:
                safe_coordinates = (x + 1, y + 1)
                safe_label = COORDINATE_LABEL_MAP[safe_coordinates]
                safe_positions.add(safe_label)
    return safe_positions


def safe_pawns(pawns: set) -> int:
    safe_positions = _get_safe_positions(pawns)
    safe_pawns = pawns.intersection(safe_positions)
    return len(safe_pawns)
