# pylint: disable=missing-module-docstring

from typing import Iterable, List, Any, Iterator, Union


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

    def __getitem__(self, index: Union[int, slice]) -> Any:
        # Since we want to support both indexing and slicing on the
        # SortedFrozenSet object, the passed in index could be either an
        # integer or a slice object. When index is an integer, we can
        # simply return the element. However, when index is a slice object
        # we want to return a SortedFrozenSet object. Hence, we need to be
        # careful about, how we treat the provided index object.
        res = self._items[index]
        return (
            SortedFrozenSet(items=res)
            if isinstance(index, slice)
            else res
        )

    def __repr__(self) -> str:
        return '{type}(items={args})'.format(type=self.__class__.__name__,
                                             args=(
                                                 repr(self._items)
                                                 if self._items else ''
                                             ))

    def __eq__(self, other: Any) -> bool:
        # This type checking is introduced in order to reason with the test
        # EqualityTest().test_type_mismatch. In this test we want to compare
        # a SortedFrozenSet object against a completely different object, and
        # therefore, we need a completely different equality implementation.
        # Hence, we return the NotImplemented object instead of raising the
        # same.
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items # noqa


if __name__ == '__main__':
    pass


