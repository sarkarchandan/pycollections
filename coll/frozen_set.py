# pylint: disable=missing-module-docstring

from typing import Iterable, List, Any, Iterator


class SortedFrozenSet:

    _items: List[Any]

    def __init__(self, items: Iterable = None) -> None:
        self._items = sorted(
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

    def __iter__(self) -> Iterator:
        return iter(self._items)
        # Following code is also valid for passing our test case. In this
        # approach we make use of the Generator objects. A function, that
        # has one or more yield statement is a Generator function, and a
        # Generator function also produces an Iterator.
        # for item in self._items:
        #     yield item


if __name__ == '__main__':
    pass


