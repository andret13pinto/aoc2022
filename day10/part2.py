from __future__ import annotations

import sys
import textwrap

DIRS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}


def parse_input(input_path: str) -> list[str]:
    with open(input_path) as input:
        return input.read().splitlines()


def main(input_path: str) -> str:
    lines = parse_input(input_path)
    sprite_pos = 1
    clock = 0
    draw = ''
    for line in lines:
        if line == 'noop':
            if abs(sprite_pos - clock % 40) <= 1:
                draw += '#'
            else:
                draw += '.'
            clock += 1
        if line.startswith('addx'):
            value = line.split(' ')[1]
            for _ in range(2):
                if abs(sprite_pos - clock % 40) <= 1:
                    draw += '#'
                else:
                    draw += '.'
                clock += 1
            sprite_pos += int(value)
    return '\n'.join(textwrap.wrap(draw, 40))


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
