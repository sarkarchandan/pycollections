# pylint: disable=missing-module-docstring

from __future__ import annotations

from typing import Iterable, Tuple, Any, Iterator, Union, List
from collections.abc import Sequence
from itertools import chain
from bisect import bisect_left


class SortedFrozenSet(Sequence):

    _items: Tuple[Any]

    def __init__(self, items: Iterable = None) -> None:
        srt: List[Any] = sorted(
            # Using set as an intermediate collection serves an important
            # purpose. Set is a collection of distinct elements or null.
            # Using set gets rid of any duplicate items, that the provided
            # Iterable might have.
            set(items) if (items is not None)
            else set()
        )
        self._items = tuple(srt)

    def __contains__(self, item: Any) -> bool:
        # We first search, which is the right index for inserting the item
        # so that the sorted order of the collection is preserved.
        index: int = bisect_left(self._items, item)
        # If the index is equal to the length of the self._items, that would
        # mean, the item is non-existing, and needs to be inserted at the very
        # end in order to insert the sorted order. And we also check if the
        # item at the current index is the one, we are concerned with. This
        # works because the underlying collection is a collection of distinct
        # elements.
        return index != len(self._items) and self._items[index] == item

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
        # Since we have refactored our internal collection self._items to a
        # tuple in order to support the Hashable protocol, we need to make
        # some adjustments here in order to generate the string representation
        # of the object construction. The SortedFrozenSet object is possible
        # to construct with any Iterable such as a list. Our testcases cover
        # that.
        return '{type}(items={args})'.format(type=self.__class__.__name__,
                                             args=(
                                                 '[{}]'.format(
                                                     ', '.join(map(repr,
                                                                   self._items))
                                                 )
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

    def __hash__(self) -> int:
        # One easy way to create a hashcode out of multiple hashable objects
        # is to put them inside a tuple, and call the hash function on the
        # tuple. However, in this case we would also change the type of the
        # internal self._items to a tuple instead, because list objects is
        # mutable in Python, and should not have a hash value.
        return hash(
            (type(self), self._items)
        )

    def __add__(self, other: Any) -> SortedFrozenSet:
        if not isinstance(other, type(self)):
            # Our use of NotImplemented here has a similar reason as before.
            # Since we are supposed to return a concrete SortedFrozenSet object
            # from this method, when we are not doing it, Python treats the same
            # as TypeError due to wrong type.
            return NotImplemented
        return SortedFrozenSet(
            items=chain(self._items, other._items)
        )

    def __mul__(self, rhs: int) -> SortedFrozenSet:
        # When the right-hand side operand is 0 or less, we can simply return
        # self, because our object us immutable. If this was a mutable object
        # instead, we would have returned a copy of the object after due
        # operation.
        return self if rhs > 0 else SortedFrozenSet()

    def __rmul__(self, lhs: int) -> SortedFrozenSet:
        # Since our object is immutable, in this case multiplication from
        # left or right-hand side are same. Hence, we can simply delegate
        # to the __mul__ method implementation.
        return self * lhs

    def count(self, item: Any) -> int:
        # Overrides the base implementation of the count methods from the
        # Sequence base class. We delegate to the __contains__ method
        # implementation, which make use of the binary search utility of the
        # bisect module, and achieve O(log n) runtime complexity with the
        # searching an item in our ordered collection of distinct elements.
        return int(item in self)

    def index(self, item: Any, start: int = ..., stop: int = ...) -> int:
        # Overrides the base implementation of the index methods using the
        # binary search.
        index: int = bisect_left(self._items, item)
        if index != len(self._items) and self._items[index] == item:
            return index
        raise ValueError(f'{item!r} not found')


if __name__ == '__main__':
    pass


