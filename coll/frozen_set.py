# pylint: disable=missing-module-docstring

from typing import Iterable, Tuple, Any


class SortedFrozenSet:

    _items: Tuple[Any]

    def __init__(self, items: Iterable = None) -> None:
        self._items = tuple(
            # Using set as an intermediate collection serves an important
            # purpose. Set is a collection of distinct elements or null.
            # Using set gets rid of any duplicate items, that the provided
            # Iterable might have.
            set(items) if (items is not None)
            else set()
        )

    def __contains__(self, item: Any) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)


if __name__ == '__main__':
    pass


