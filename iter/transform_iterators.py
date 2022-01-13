from typing import Any, List, Dict, Iterator, Iterable


typesetting_table: Dict[str, str] = {
    '-': '\u2212',
    '*': '\u00D7',
    '/': '\u00F7',
}


class TranslationIterator:

    _iterator: Iterator
    _table: Dict[str, str]

    def __init__(self, typ_tab: Dict[str, str], itr: Iterable) -> None:
        self._table = typ_tab
        self._iterator = iter(itr)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        # Here we are using a similar idea, which we did for the filtering
        # iterator as well. We are calling the next function on the internal
        # iterator. That means, eventually StopIteration would be raised, which
        # we'd propagate here.
        item: Any = next(self._iterator)
        return self._table.get(item, item)


if __name__ == '__main__':
    # In this demonstration we don't focus on the binary tree. Rather we take
    # an Infix expression in machine-readable language, and translate the same
    # to humanreadable language.
    iter_exp: List[str] = ['p', '*', 'q', '-', 'r', '/', 's', '+', 't']
    # We want to translate this to p × q − r ÷ s + t
    trn_iter: TranslationIterator = TranslationIterator(
        typ_tab=typesetting_table, itr=iter_exp)
    joined: str = ' '.join(trn_iter)
    print(f'Original machine-readable expression: {iter_exp}')
    print(f'Translated humanreadable expression: {joined}')

