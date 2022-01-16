# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import unittest
from unittest import TestCase
from typing import List, Iterator
from frozen_set import SortedFrozenSet


class ConstructionTestCase(TestCase):

    def test_construct_empty(self) -> None:
        try:
            _ = SortedFrozenSet(items=[])
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet with empty list')

    def test_construct_from_list(self) -> None:
        try:
            _ = SortedFrozenSet(items=[4, 1, 6, 3, 10])
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet with nonempty list')

    def test_construct_from_iterator(self) -> None:
        iter_list: List[int] = [4, 1, 6, 3, 10]
        iterator: Iterator = iter(iter_list)
        try:
            _ = SortedFrozenSet(items=iterator)
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet with iterator')

    def test_construct_no_args(self) -> None:
        try:
            _ = SortedFrozenSet()
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet without arguments')


class ContainerTestCase(TestCase):

    _set: SortedFrozenSet

    def setUp(self) -> None:
        self._set = SortedFrozenSet(items=[6, 7, 3, 9])

    def test_positive_contained(self) -> None:
        self.assertTrue(7 in self._set)

    def test_negative_contained(self) -> None:
        self.assertFalse(5 in self._set)

    def test_positive_not_contained(self) -> None:
        self.assertTrue(5 not in self._set)

    def test_negative_not_contained(self) -> None:
        self.assertFalse(3 not in self._set)


class SizedTestCase(TestCase):

    def test_empty_with_default(self) -> None:
        fs: SortedFrozenSet = SortedFrozenSet()
        self.assertEqual(len(fs), 0)

    def test_empty(self) -> None:
        fs: SortedFrozenSet = SortedFrozenSet(items=[])
        self.assertEqual(len(fs), 0)

    def test_one(self) -> None:
        fs: SortedFrozenSet = SortedFrozenSet(items=[23])
        self.assertEqual(len(fs), 1)

    def test_multiple(self) -> None:
        fs: SortedFrozenSet = SortedFrozenSet(items=range(10))
        self.assertEqual(len(fs), 10)

    def test_with_duplicates(self) -> None:
        # This test validates a fundamental set behavior, that set is a
        # collection of distinct items.
        fs: SortedFrozenSet = SortedFrozenSet(items=[5, 4, 5, 5, 6])
        self.assertEqual(len(fs), 3)


if __name__ == '__main__':
    unittest.main()
