from typing import Iterable, Any, Iterator, List
from basic_iterators import InOrderIterator


missing: object = object()


class SkipMissingIterator:

    _iterator: Iterator

    def __init__(self, iterable: Iterable) -> None:
        self._iterator = iter(iterable)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        # In this implementation, we are calling next on the underlying
        # iterator, and checking if the retrieved object is the sentinel
        # object. We can simply check the sentinel objects like this,
        # because we are creating just one instance of the object globally.
        # If the underlying iterator exhausts and throws StopIteration, we
        # can let it propagate because that is expected behavior.
        while True:
            item: Any = next(self._iterator)
            if item is not missing:
                return item


if __name__ == '__main__':
    # In this example our infix expression is r * p + q
    # This results in the following imperfect binary tree
    #               *
    #           r       +
    #               p       q
    # We can transform this binary tree using the sentinel objects like
    # this.
    #                     *
    #           r                   +
    #    missing  missing      p       q
    # And the tre expression becomes [* r   +   missing missing p   q]
    iter_exp: List[Any] = ['*', 'r', '+', missing, missing, 'p', 'q']
    smi: SkipMissingIterator = SkipMissingIterator(iterable=iter_exp)
    print(f'List representation of the SkipMissingIterator: {list(smi)}')
    smi: SkipMissingIterator = SkipMissingIterator(
        iterable=InOrderIterator(iter_exp))
    joined: str = ' '.join(smi)
    print(f'String representation of the filtered expression: {joined}')
    pass
