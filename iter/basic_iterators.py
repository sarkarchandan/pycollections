from typing import List, Iterator, Any, Sequence
from argparse import ArgumentParser, Namespace


def _is_perfect_length(seq: Sequence) -> bool:
    """Returns True if the length of the provided sequence is 2^n-1, False
    otherwise.

    :param seq: Sequence to be checked for perfect length
    :type seq: Sequence
    :return: If provided sequence has perfect length
    :rtype: bool
    """
    n: int = len(seq)
    return ((n + 1) & n == 0) and (n != 0)


def _left_child_index_of(idx: int) -> int:
    """Returns the index of the left child of the element in the provided
    index.

    :param idx: Provided index of a given element
    :type: int
    :return: Index of the left child
    :rtype: int
    """
    return 2 * idx + 1


def _right_child_index_of(idx: int) -> int:
    """Returns the index of the right child of the element in the provided
    index.

    :param idx: Provided index of a given element
    :type: int
    :return: Index of the right child
    :rtype: int
    """
    return 2 * idx + 2


class LevelOrderIterator:
    _seq: Sequence
    _idx: int

    def __init__(self, seq: Sequence) -> None:
        if not _is_perfect_length(seq=seq):
            raise ValueError(f'Sequence of length {len(seq)} does not '
                             f'represent a perfect binary tree')
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


class PreOrderIterator:
    """For the preorder traversal we need a stack to keep track of the indices.
    Python does not have a stack out of the box. However, we can simulate one
    using the ist methods.
    """

    _seq: Sequence
    _stack: List[int]

    def __init__(self, seq: Sequence) -> None:
        if not _is_perfect_length(seq=seq):
            raise ValueError(f'Sequence of length {len(seq)} does not '
                             f'represent a perfect binary tree')
        self._seq = seq
        self._stack = [0]

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        # Exit condition - If the stack is empty, we have no more elements to
        # iterate over.
        if len(self._stack) == 0:
            raise StopIteration
        idx: int = self._stack.pop()
        res: Any = self._seq[idx]
        # Ensure preorder traversal by first pushing the right child index,
        # followed by the left child to the left child index to the stack.
        # Because the sack is LIFO data structure, while popping from the stack
        # in the next call, we'd get the left child index first, followed by the
        # right child index in the subsequent call.
        right_idx: int = _right_child_index_of(idx)
        if right_idx < len(self._seq):
            self._stack.append(right_idx)
        left_idx: int = _left_child_index_of(idx)
        if left_idx < len(self._seq):
            self._stack.append(left_idx)
        return res


class InOrderIterator:
    """For the inorder traversal we need a stack to keep track of the indices.
    Python does not have a stack out of the box. However, we can simulate one
    using the ist methods.
    """

    _seq: Sequence
    _stack: List[int]
    _idx: int

    def __init__(self, seq: Sequence) -> None:
        if not _is_perfect_length(seq=seq):
            raise ValueError(f'Sequence of length {len(seq)} does not '
                             f'represent a perfect binary tree')
        self._seq = seq
        self._stack = []
        self._idx = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        # Exit condition - Now we have a more complex exit condition. We keep 
        # track of the currently running index as well as the stack, and we 
        # exit, iff stack is empty and the index is out of bound of the 
        # sequence.
        if len(self._stack) == 0 and self._idx >= len(self._seq):
            raise StopIteration
        # We iteratively look for the left child in each subtree from our 
        # sequence, using the _idx attribute, and we'd stop only when the 
        # _idx goes out of bound of the sequence. This iteration would
        # stop, when we reach the left most leaf node of a subtree.
        while self._idx < len(self._seq):
            self._stack.append(self._idx)
            self._idx = _left_child_index_of(self._idx)
        # When we have reached at the leaf node, and now we pop the
        # last pushed index from the stack, and corresponding, and we are going
        # to yield the corresponding element.
        idx: int = self._stack.pop()
        res: Any = self._seq[idx]
        # Finally, we are going to point right child index of the retrieved
        # index to he _idx attribute, which the Iterator keep track of.
        self._idx = _right_child_index_of(idx)
        return res


if __name__ == '__main__':
    # Expression in Infix notation: (a + b) * (c - d)
    # Expression represented as a binary search tree.
    #                   *
    #           +               -
    #       a       b       c       d
    #      [*   +   -   a   b   c   d] <- This is the level order expression
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
        joined: str = ' '.join(lvl_itr)
        print(f'Expression joined using the LevelOrderIterator as Iterable'
              f': {joined}')
    elif args.target == 'pre_order_iterable':
        #                   *
        #           +               -
        #       a       b       c       d
        #      [*   +   -   a   b   c   d] <- This is the level order expression
        #      [*   +   a   b   -   c   d <- This is the preorder expression
        # We need to verify, whether we are getting the preorder expression
        # from the PreOrderIterator upon using level order expression as the
        # input sequence.
        print('Demonstrate PreOrderIterator as an Iterable')
        pre_itr: PreOrderIterator = PreOrderIterator(seq=iter_exp)
        joined: str = ' '.join(pre_itr)
        print(f'Expression joined using the PreOrderIterator as Iterable: '
              f'{joined}')
    elif args.target == 'in_order_iterable':
        #                   *
        #           +               -
        #       a       b       c       d
        #      [*   +   -   a   b   c   d] <- This is the level order expression
        #      [*   +   a   b   -   c   d <- This is the preorder expression
        #      [a   +   b   *   c   -   d] <- This is the inorder expression
        # We need to verify, whether we are getting the inorder expression
        # from the InOrderIterator upon using level order expression as the
        # input sequence. The result of the InOrderIterator is our good old
        # human-readable Infix notation.
        print('Demonstrate InOrderIterator as an Iterable')
        in_itr: InOrderIterator = InOrderIterator(seq=iter_exp)
        joined: str = ' '.join(in_itr)
        print(f'Expression joined using the InOrderIterator as Iterable: '
              f'{joined}')
    else:
        raise ValueError('Unsupported value provided as argument')
