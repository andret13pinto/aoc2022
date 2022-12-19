from __future__ import annotations

import ast
import sys
from functools import cmp_to_key
from itertools import zip_longest


def parse_input(input_path: str) -> list[list]:
    lines = []
    with open(input_path) as file:
        for line in file.read().splitlines():
            if len(line) > 0:
                lines.append(ast.literal_eval(line))
    lines.append([[2]])
    lines.append([[6]])
    return lines


def compare_pair(pair1: list, pair2: list) -> int:
    for value_l, value_r in zip_longest(pair1, pair2):
        if value_l is None:
            return -1
        elif value_r is None:
            return 1
        elif type(value_l) is int and type(value_r) is int:
            if value_l < value_r:
                return -1
            elif value_l > value_r:
                return 1
            else:
                continue
        elif type(value_l) is list and type(value_r) is list:
            result = compare_pair(value_l, value_r)
            if result == -1:
                return -1
            elif result == 0:
                continue
            else:
                return 1
        elif type(value_l) is list and type(value_r) is int:
            result = compare_pair(value_l, [value_r])
            if result == -1:
                return -1
            elif result == 0:
                continue
            else:
                return 1
        elif type(value_l) is int and type(value_r) is list:
            result = compare_pair([value_l], value_r)
            if result == -1:
                return -1
            elif result == 0:
                continue
            else:
                return 1
        else:
            raise NotImplementedError('Not supposed to reach')
    else:
        return 0


def main(input_path: str) -> int:
    lines = parse_input(input_path)
    lines = sorted(lines, key=cmp_to_key(compare_pair))
    return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
