from __future__ import annotations

import ast
import sys
from itertools import zip_longest


def parse_input(input_path: str) -> list[list]:
    pairs = []
    with open(input_path) as file:
        for pair in file.read().split('\n\n'):
            lines = []
            for line in pair.splitlines():
                lines.append(ast.literal_eval(line))
            pairs.append(lines)
    return pairs


def compare_pair(pair: list) -> int:
    for value_l, value_r in zip_longest(pair[0], pair[1]):
        if value_l is None:
            return 1
        elif value_r is None:
            return 0
        elif type(value_l) is int and type(value_r) is int:
            if value_l < value_r:
                return 1
            elif value_l > value_r:
                return 0
            else:
                continue
        elif type(value_l) is list and type(value_r) is list:
            result = compare_pair([value_l, value_r])
            if result == 1:
                return 1
            elif result == 2:
                continue
            else:
                return 0
        elif type(value_l) is list and type(value_r) is int:
            result = compare_pair([value_l, [value_r]])
            if result == 1:
                return 1
            elif result == 2:
                continue
            else:
                return 0
        elif type(value_l) is int and type(value_r) is list:
            result = compare_pair([[value_l], value_r])
            if result == 1:
                return 1
            elif result == 2:
                continue
            else:
                return 0
        else:
            raise NotImplementedError('Not supposed to reach')
    else:
        return 2


def main(input_path: str) -> int:
    pairs = parse_input(input_path)
    count = 0
    for index, pair in enumerate(pairs):
        if compare_pair(pair):
            count += index + 1
    return count


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
