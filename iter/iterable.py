# pylint: disable=missing-module-docstring

from typing import Iterable, Iterator, Tuple, Any, List
from basic_iterators import InOrderIterator, _is_perfect_length
from filter_iterators import SkipMissingIterator
from argparse import ArgumentParser, Namespace


class PerfectBinaryTree:

    _lo_iterable: Tuple[Any]

    def __init__(self, level_order_iterable: Iterable) -> None:
        self._lo_iterable = tuple(level_order_iterable)
        if not _is_perfect_length(seq=self._lo_iterable):
            raise ValueError(f'Sequence of length {len(self._lo_iterable)} '
                             f'does not represent a perfect binary tree')

    def __iter__(self) -> Iterator:
        return SkipMissingIterator(InOrderIterator(self._lo_iterable))


if __name__ == '__main__':
    # In this demonstration, we are going to create simple custom Iterable
    # using the previous constructs, which we have created while demonstrating
    # the Iterator protocol.
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('target', help='Designates the kind of demonstration',
                        type=str)
    args: Namespace = parser.parse_args()
    iter_exp: List[str] = '+ * / u v w x'.split(' ')
    pbt: PerfectBinaryTree = PerfectBinaryTree(level_order_iterable=iter_exp)
    if args.target == 'iterable_as_is':
        joined: str = ' '.join(pbt)
        print(f'The inorder representation created by Iterable is: {joined}')
    elif args.target == 'iterator_from_iterable':
        print(f'Using iterable as iterator...')
        itr: Iterator = iter(pbt)
        for item in itr:
            print(item)
    else:
        raise ValueError('Unsupported value provided as argument')

