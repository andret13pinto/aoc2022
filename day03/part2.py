from __future__ import annotations

import string
import sys


def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines


def find_repeated_item(sack_list: list[str]) -> str:
    sack_iventory: list = [set(), set(), set()]
    for elf, sack in enumerate(sack_list):
        for item in sack:
            sack_iventory[elf].add(item)
    return set.intersection(*sack_iventory).pop()


def main(input_path: str) -> int:
    lines = parse_inpute(input_path)
    sum_priorities = 0
    value_dict = {
        letter: value + 1 for value,
        letter in enumerate(string.ascii_letters)
    }
    it = iter(lines)
    for sack in it:
        item = find_repeated_item([sack, next(it), next(it)])
        sum_priorities += value_dict[item]
    return sum_priorities


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
