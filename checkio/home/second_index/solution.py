from typing import Optional


def second_index(text: str, symbol: str) -> Optional[int]:
    first_idx = text.find(symbol)
    second_idx = text.find(symbol, first_idx + 1)
    return second_idx if second_idx != -1 else None
