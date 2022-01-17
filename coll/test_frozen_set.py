# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import unittest
from unittest import TestCase
from typing import List, Iterator, Container, Sized, Sequence, Hashable
from typing import Iterable
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

    def test_protocol(self) -> None:
        self.assertTrue(issubclass(SortedFrozenSet, Container))


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

    def test_protocol(self) -> None:
        self.assertTrue(issubclass(SortedFrozenSet, Sized))


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

    def test_protocol(self) -> None:
        self.assertTrue(issubclass(SortedFrozenSet, Iterable))


class SequenceTestCase(TestCase):

    _set: SortedFrozenSet

    def setUp(self) -> None:
        self._set = SortedFrozenSet(items=[1, 4, 9, 13, 15])

    # Following testcases would cover the use of single integer indexing
    # with the SortedFrozenSet.
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

    # Following test case validates the support for reversed Iterator for the
    # SortedFrozenSet type.
    def test_reversed(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet(items=[1, 3, 5, 7])
        rev: Iterator = reversed(s)
        self.assertEqual(next(rev), 7)
        self.assertEqual(next(rev), 5)
        self.assertEqual(next(rev), 3)
        self.assertEqual(next(rev), 1)
        with self.assertRaises(StopIteration):
            _ = next(rev)

    # Following testcases would cover the possibility of finding the index
    # of a given item in the SortedFrozenSet.
    def test_index_positive(self) -> None:
        self.assertEqual(self._set.index(9), 2)

    def test_index_negative(self) -> None:
        with self.assertRaises(ValueError):
            _ = self._set.index(17)

    # Following testcases would cover the possibility of having a count of
    # specific elements in the SortedFrozenSet. However, this is utility is
    # implemented purely for the sake of completing the Sequence protocol,
    # because we know, that a set is collection of distinct elements. Hence,
    # an item would either exist in a set or won't exist at all.
    def test_count_zero(self) -> None:
        self.assertEqual(self._set.count(34), 0)

    def test_count_one(self) -> None:
        self.assertEqual(self._set.count(9), 1)

    # Following test cases cover the addition of two SortedFrozenSets
    # using the set union and set intersection methods.
    def test_add_disjoint(self) -> None:
        s1: SortedFrozenSet = SortedFrozenSet(items=[1, 2, 3])
        s2: SortedFrozenSet = SortedFrozenSet(items=[5, 4, 6])
        self.assertEqual(s1 + s2, SortedFrozenSet(items=[1, 2, 3, 4, 5, 6]))

    def test_add_equal(self) -> None:
        self.assertEqual(self._set + self._set, self._set)

    def test_add_intersecting(self) -> None:
        s1: SortedFrozenSet = SortedFrozenSet(items=[1, 2, 3])
        s2: SortedFrozenSet = SortedFrozenSet(items=[3, 4, 6])
        self.assertEqual(s1 + s2, SortedFrozenSet(items=[1, 2, 3, 4, 6]))

    def test_add_type_error_left(self) -> None:
        with self.assertRaises(TypeError):
            _ = self._set + (3, 5, 8)

    def test_add_type_error_right(self) -> None:
        with self.assertRaises(TypeError):
            _ = (3, 5, 8) + self._set # noqa

    # Following testcases cover the scenario for repeating elements of the
    # SortedFrozenSet.
    def test_repetition_zero_right(self) -> None:
        self.assertEqual(self._set * 0, SortedFrozenSet())

    def test_repetition_negative_right(self) -> None:
        self.assertEqual(self._set * -1, SortedFrozenSet())

    def test_repetition_nonzero_right(self) -> None:
        self.assertEqual(self._set * 100, self._set)

    def test_repetition_zero_left(self) -> None:
        self.assertEqual(0 * self._set, SortedFrozenSet())

    def test_repetition_negative_left(self) -> None:
        self.assertEqual(-1 * self._set, SortedFrozenSet())

    def test_repetition_nonzero_left(self) -> None:
        self.assertEqual(100 * self._set, self._set)

    def test_protocol(self) -> None:
        self.assertTrue(issubclass(SortedFrozenSet, Sequence))


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


class HashableTestCase(TestCase):

    def test_equal_sets_have_same_hashcode(self) -> None:
        self.assertEqual(hash(SortedFrozenSet(items=[5, 2, 1, 4])),
                         hash(SortedFrozenSet(items=[4, 1, 5, 2])))

    def test_protocol(self) -> None:
        self.assertTrue(issubclass(SortedFrozenSet, Hashable))


if __name__ == '__main__':
    unittest.main()
