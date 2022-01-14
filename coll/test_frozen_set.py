# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import unittest
from unittest import TestCase
from typing import List, Iterator
from frozen_set import SortedFrozenSet


class SortedFrozenSetTestCase(TestCase):

    def test_construct_empty(self) -> None:
        try:
            _ = SortedFrozenSet(seq=[])
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet with empty list')

    def test_construct_from_list(self) -> None:
        try:
            _ = SortedFrozenSet(seq=[4, 1, 6, 3, 10])
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet with nonempty list')

    def test_construct_from_iterator(self) -> None:
        iter_list: List[int] = [4, 1, 6, 3, 10]
        iterator: Iterator = iter(iter_list)
        try:
            _ = SortedFrozenSet(seq=iterator)
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet with iterator')

    def test_construct_no_args(self) -> None:
        try:
            _ = SortedFrozenSet()
        except TypeError:
            self.fail('Failed to construct SortedFrozenSet without arguments')


if __name__ == '__main__':
    unittest.main()
