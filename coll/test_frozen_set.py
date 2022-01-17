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


class IterableTestCase(TestCase):

    _set: SortedFrozenSet

    def setUp(self) -> None:
        self._set = SortedFrozenSet(items=[7, 2, 1, 1, 9])

    def test_iter(self) -> None:
        sit: Iterator = iter(self._set)
        self.assertEqual(next(sit), 1)
        self.assertEqual(next(sit), 2)
        self.assertEqual(next(sit), 7)
        self.assertEqual(next(sit), 9)
        with self.assertRaises(StopIteration):
            next(sit)

    def test_for_loop(self) -> None:
        exp: List[int] = [1, 2, 7, 9]
        idx: int = 0
        for item in self._set:
            self.assertEqual(item, exp[idx])
            idx += 1


class SequenceTestCase(TestCase):

    _set: SortedFrozenSet

    def setUp(self) -> None:
        self._set = SortedFrozenSet(items=[1, 4, 9, 13, 15])

    def test_index_zero(self) -> None:
        self.assertEqual(self._set[0], 1)

    def test_index_four(self) -> None:
        self.assertEqual(self._set[4], 15)

    def test_index_one_beyond_the_end(self) -> None:
        with self.assertRaises(IndexError):
            _ = self._set[5]

    def test_index_minus_one(self) -> None:
        self.assertEqual(self._set[-1], 15)

    def test_index_minus_five(self) -> None:
        self.assertEqual(self._set[-5], 1)

    def test_index_one_before_the_start(self) -> None:
        with self.assertRaises(IndexError):
            _ = self._set[-6]

    # Following set of tests concerning slicing leads to a design decision, that
    # upon slicing from a SortedFrozenSet object, what we expect, is again a
    # SortedFrozenSet, and not any other structure. This is one of the benefits
    # of the TDD approach. We can be concrete, and consistent about, how we
    # want our implementation to behave. This mitigates the possibility of the
    # undesired surprises later.
    def test_slice_from_start(self) -> None:
        self.assertEqual(self._set[:3], SortedFrozenSet(items=[1, 4, 9]))

    def test_slice_to_end(self) -> None:
        self.assertEqual(self._set[3:], SortedFrozenSet(items=[13, 15]))

    def test_slice_empty(self) -> None:
        self.assertEqual(self._set[10:], SortedFrozenSet())

    def test_slice_arbitrary(self) -> None:
        self.assertEqual(self._set[2:4], SortedFrozenSet(items=[9, 13]))

    def test_slice_step(self) -> None:
        self.assertEqual(self._set[0:5:2], SortedFrozenSet(items=[1, 9, 15]))

    def test_slice_full(self) -> None:
        self.assertEqual(self._set[:], self._set)


class ReprTestCase(TestCase):

    def test_repr_empty(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet()
        self.assertEqual(repr(s), 'SortedFrozenSet(items=)')

    def test_repr_one(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet(items=[45, 76, 23])
        self.assertEqual(repr(s), 'SortedFrozenSet(items=[23, 45, 76])')


class EqualityTestCase(TestCase):

    def test_positive_equal(self) -> None:
        self.assertTrue(SortedFrozenSet(items=[4, 5, 6]) ==
                        SortedFrozenSet(items=[6, 5, 4]))

    def test_negative_equal(self) -> None:
        self.assertFalse(SortedFrozenSet(items=[4, 5, 6]) ==
                         SortedFrozenSet(items=[1, 2, 4]))

    def test_type_mismatch(self) -> None:
        self.assertFalse(SortedFrozenSet(items=[4, 5, 6]) == [4, 5, 6])

    def test_identical(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet(items=[10, 11, 12])
        self.assertTrue(s == s)


class InequalityTestCase(TestCase):

    def test_positive_unequal(self) -> None:
        self.assertTrue(SortedFrozenSet(items=[4, 5, 6]) !=
                        SortedFrozenSet(items=[1, 2, 4]))

    def test_negative_unequal(self) -> None:
        self.assertFalse(SortedFrozenSet(items=[4, 5, 6]) !=
                         SortedFrozenSet(items=[6, 5, 4]))

    def test_type_mismatch(self) -> None:
        self.assertTrue(SortedFrozenSet(items=[1, 2, 3]) != [1, 2, 3])

    def test_identical(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet(items=[10, 11, 12])
        self.assertFalse(s != s)


if __name__ == '__main__':
    unittest.main()
