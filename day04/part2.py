from __future__ import annotations

import sys


def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines


def not_overlap(x: tuple[int, int], y: tuple[int, int]) -> bool:
    if x[1] < y[0] or y[1] < x[0]:
        return True
    else:
        return False


def main(input_path: str) -> int:
    lines = parse_inpute(input_path)
    s = 0
    for line in lines:
        x_str, y_str = line.split(',')
        x = (int(x_str.split('-')[0]), int(x_str.split('-')[1]))
        y = (int(y_str.split('-')[0]), int(y_str.split('-')[1]))
        if not_overlap(x, y):
            s += 1
    return len(lines) - s


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
