from typing import List, Iterator


if __name__ == '__main__':
    # Expression in Infix notation: (a + b) * (c - d)
    # Expression represented as a binary search tree.
    #                   *
    #           +               -
    #       a       b       c       d
    # [*   +   -   a   b   c   d]
    iter_exp: List[str] = ['*', '+', '-', 'a', 'b', 'c', 'd']
    print('Using iterator as iterable with for loop.')
    list_iterator: Iterator = iter(iter_exp)
    for char in list_iterator:
        print(char)
    print('Demonstrate the next function, and the way it works.')
    list_iterator: Iterator = iter(iter_exp)
    try:
        while True:
            print(next(list_iterator))
    except StopIteration:
        print('StopIteration error raised')
