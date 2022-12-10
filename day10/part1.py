from __future__ import annotations

import sys

DIRS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}


def parse_input(input_path: str) -> list[str]:
    with open(input_path) as input:
        return input.read().splitlines()


def main(input_path: str) -> int:
    lines = parse_input(input_path)
    values = [1]
    for line in lines:
        if line == 'noop':
            values.append(values[-1])
        if line.startswith('addx'):
            value = line.split(' ')[1]
            values.extend([values[-1], values[-1] + int(value)])
    return (
        values[19] * 20 + values[59] * 60 + values[99] * 100
        + values[139] * 140 + values[179] * 180 + values[219] * 220
    )


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
