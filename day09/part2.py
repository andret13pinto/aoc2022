from __future__ import annotations

import sys

DIRS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}


def parse_input(input_path: str) -> list[str]:
    with open(input_path) as input:
        return input.read().splitlines()


def add_tuples(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def find_direction(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    dir_ = (0, 0)
    if head[0] - tail[0] > 1:
        dir_ = add_tuples(dir_, DIRS['R'])
        if head[1] - tail[1] >= 1:
            dir_ = add_tuples(dir_, DIRS['U'])
        elif tail[1] - head[1] >= 1:
            dir_ = add_tuples(dir_, DIRS['D'])
    elif head[1] - tail[1] > 1:
        dir_ = add_tuples(dir_, DIRS['U'])
        if head[0] - tail[0] >= 1:
            dir_ = add_tuples(dir_, DIRS['R'])
        elif tail[0] - head[0] >= 1:
            dir_ = add_tuples(dir_, DIRS['L'])
    elif tail[1] - head[1] > 1:
        dir_ = add_tuples(dir_, DIRS['D'])
        if head[0] - tail[0] >= 1:
            dir_ = add_tuples(dir_, DIRS['R'])
        elif tail[0] - head[0] >= 1:
            dir_ = add_tuples(dir_, DIRS['L'])
    elif tail[0] - head[0] > 1:
        dir_ = add_tuples(dir_, DIRS['L'])
        if head[1] - tail[1] >= 1:
            dir_ = add_tuples(dir_, DIRS['U'])
        elif tail[1] - head[1] >= 1:
            dir_ = add_tuples(dir_, DIRS['D'])
    return dir_


def main(input_path: str) -> int:
    input = parse_input(input_path)
    visited = [(0, 0)]
    knots = [(0, 0)]*10
    for line in input:
        dir_, dist = line.split(' ')
        for _ in range(int(dist)):
            knots[0] = add_tuples(knots[0], DIRS[dir_])
            for nr in range(1, len(knots)):
                k_dir = find_direction(knots[nr-1], knots[nr])
                knots[nr] = add_tuples(knots[nr], k_dir)
                if nr == 9:
                    visited.append(knots[nr])
    return len(set(visited))


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
