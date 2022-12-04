from __future__ import annotations

import sys


def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines


def calculate_calories(input_path: str) -> int:
    lines = parse_inpute(input_path)
    current_max = 0
    current_sum = 0
    for line in lines:
        if line == '':
            if current_sum > current_max:
                current_max = current_sum
            current_sum = 0
        else:
            current_sum += int(line)
    return current_max


if __name__ == '__main__':
    print(calculate_calories('input.txt'))
    sys.exit(0)
