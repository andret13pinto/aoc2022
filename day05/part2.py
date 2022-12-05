from __future__ import annotations

import sys


def parse_stacks(input_path: str) -> tuple[int, list[str]]:
    with open(input_path) as input:
        first_line = input.readline()
        nr_stacks = (len(first_line.rstrip('\n')) + 1)//4
    with open(input_path) as input:
        lines = [line.rstrip('\n') for line in input]
    return nr_stacks, lines


def parse_commands(input_path: str) -> list[list[int]]:
    lines = []
    with open(input_path) as input:
        for line in input:
            lines.append([
                int(line.split(' ')[1]),
                int(line.split(' ')[3]),
                int(line.split(' ')[5])
            ])
    return lines


def populate_stacks(nr_stacks: int, lines: list[str]) -> list[list]:
    stacks = [[] for _ in range(nr_stacks)]
    pos_map = {4*pos + 1: pos for pos in range(nr_stacks)}
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            return stacks
        for pos, char in enumerate(line):
            if pos in pos_map.keys() and str.isalpha(char):
                stacks[pos_map[pos]].append(char)


def move_crates(stacks: list[list], commands: list[list[int]]) -> list[list]:
    for (nr, frm, to) in commands:
        stacks[to - 1] = stacks[frm-1][:nr] + stacks[to - 1]
        del stacks[frm-1][:nr]
    return stacks


def main(input_path_stacks: str, input_path_commands: str) -> int:
    nr_stacks, lines = parse_stacks(input_path_stacks)
    stacks = populate_stacks(nr_stacks, lines)
    cmds = parse_commands(input_path_commands)
    stacks = move_crates(stacks, cmds)
    return ''.join([stack[0] for stack in stacks])


if __name__ == '__main__':
    print(main('stack_input.txt', 'commands_input.txt'))
    sys.exit(0)
