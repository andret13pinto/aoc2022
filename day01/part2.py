from __future__ import annotations

import sys


def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines


def calculate_sum_calories(input_path: str) -> int:
    lines = parse_inpute(input_path)
    lines.append('')
    calorie_list = []
    current_sum = 0
    for line in lines:
        if line == '':
            calorie_list.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    calorie_list.sort()
    return sum(calorie_list[-3:])


if __name__ == '__main__':
    print(calculate_sum_calories('input.txt'))
    sys.exit(0)
