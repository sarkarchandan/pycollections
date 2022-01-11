from typing import List, Iterator, Any, Sequence
from argparse import ArgumentParser, Namespace


class LevelOrderIterator:

    _seq: Sequence
    _idx: int

    def __init__(self, seq: Sequence) -> None:
        self._seq = seq
        self._idx = 0

    def __next__(self) -> Any:
        res: Any
        if self._idx >= len(self._seq):
            raise StopIteration
        else:
            res = self._seq[self._idx]
        self._idx += 1
        return res

    def __iter__(self) -> Iterator:
        return self


if __name__ == '__main__':
    # Expression in Infix notation: (a + b) * (c - d)
    # Expression represented as a binary search tree.
    #                   *
    #           +               -
    #       a       b       c       d
    # [*   +   -   a   b   c   d]
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('target', help='Designates the kind of demonstration',
                        type=str)
    args: Namespace = parser.parse_args()
    iter_exp: List[str] = ['*', '+', '-', 'a', 'b', 'c', 'd']
    if args.target == 'iter_for':
        print('Using iterator as iterable with for loop.')
        list_iterator: Iterator = iter(iter_exp)
        for char in list_iterator:
            print(char)
    elif args.target == 'call_next':
        print('Demonstrate the next function, and the way it works.')
        list_iterator: Iterator = iter(iter_exp)
        try:
            while True:
                print(next(list_iterator))
        except StopIteration:
            print('StopIteration error raised')
    elif args.target == 'level_order':
        print('Demonstrate the LevelOrderIterator class')
        lvl_itr: LevelOrderIterator = LevelOrderIterator(seq=iter_exp)
        try:
            while True:
                print(next(lvl_itr))
        except StopIteration:
            print('StopIteration error raised')
    elif args.target == 'level_order_iterable':
        print('Demonstrate LevelOrderIterator as an Iterable')
        lvl_itr: LevelOrderIterator = LevelOrderIterator(seq=iter_exp)
        joined: str = ''.join(lvl_itr)
        print(f'Expression joined from the Iterable: {joined}')
    else:
        raise ValueError('Unsupported value provided as argument')

