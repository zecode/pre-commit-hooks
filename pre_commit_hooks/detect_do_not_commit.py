import argparse
from typing import Optional
from typing import Sequence

BLACKLIST = [
    b'\x64\x6e\x63', #dnc
]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    bad_files = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            content = f.read()
            if any(line in content for line in BLACKLIST):
                bad_files.append(filename)

    if bad_files:
        for bad_file in bad_files:
            print(f'do not commit tag found: {bad_file}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
