from typing import (
    Any,
    List,
)


def all_the_same(elements: List[Any]) -> bool:
    return all(el == elements[0] for el in elements)
