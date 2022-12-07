from __future__ import annotations

import sys


def parse_signal(input_path: str) -> str:
    with open(input_path) as input:
        return input.readline()


def main(signal: str) -> int:
    current = []
    for pos, letter in enumerate(signal):
        current.append(letter)
        if len(current) == 15:
            del current[0]
        if len(set(current)) == 14:
            return pos + 1


if __name__ == '__main__':
    signal = parse_signal('input.txt')
    print(main(signal))
    sys.exit(0)
