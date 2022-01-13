from typing import Iterator
from fractions import Fraction


class RationalRange:
    """Implements an Iterable for the range of rational numbers with a given
    start, stop, and step values.
    """

    _step: Fraction
    _start: Fraction
    _num_steps: int
    _step: Fraction

    def __init__(self, start: int, stop: int, num_steps: int) -> None:
        if num_steps != int(num_steps):
            raise ValueError('The number of steps must have a integer value')
        if num_steps < 1:
            raise ValueError('The number of steps is not valid positive number')
        self._start = Fraction(start)
        self._num_steps = num_steps
        self._step = Fraction(stop - start, self._num_steps)

    def __getitem__(self, index: int) -> Fraction:
        if not(0 <= index < self._num_steps):
            raise IndexError
        return self._start + index * self._step


if __name__ == '__main__':
    # We demonstrate a class RationalRange, which implements the Iterable
    # protocol, without providing the implementation of the __iter__ method.
    rational_range: RationalRange = RationalRange(5, 13, 6)
    frac_iterator: Iterator = iter(rational_range)
    for frac in frac_iterator:
        print(frac)
    print(f'Using list the comprehension the iterable sequence of rational '
          f'numbers can be represented with float as: '
          f'{[float(item) for item in rational_range]}')
    print(f'These numbers sum up to: {sum(rational_range)}')




