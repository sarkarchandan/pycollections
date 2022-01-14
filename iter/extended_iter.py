from typing import Iterator, List
from argparse import ArgumentParser, Namespace
from pathlib import Path
from datetime import datetime


if __name__ == '__main__':
    # Read some line of texts from a file, strip of leading and trailing spaces
    # and convert to a sequence.
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('target', help='Designates the kind of demonstration',
                        type=str)
    args: Namespace = parser.parse_args()
    if args.target == 'generate_sequence_from_file':
        seq: List[int]
        file_path: str = Path().absolute().joinpath(
            'iter/seq_source.txt').__str__()
        with open(file_path, 'rt') as file:
            lines: Iterator = iter(lambda: file.readline().strip(), 'END')
            seq = [int(num) for num in lines]
        print(f'Generated integer sequence using iter: {seq}')
    elif args.target == 'generate_indefinite_timestamps':
        ts_iterator: Iterator = iter(lambda: datetime.now(), None)
        print('Generate five consecutive timestamps...')
        for _ in range(5):
            print(next(ts_iterator))
    else:
        raise ValueError('Unsupported value provided as argument')

