# pylint: disable=missing-module-docstring

from typing import Iterable, Tuple, Any


class SortedFrozenSet:

    _items: Tuple[Any]

    def __init__(self, items: Iterable = None) -> None:
        self._items = tuple(
            list(items) if (items is not None)
            else list()
        )

    def __contains__(self, item: Any) -> bool:
        return item in self._items


if __name__ == '__main__':
    pass


