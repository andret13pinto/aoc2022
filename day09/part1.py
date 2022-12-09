from __future__ import annotations

import sys

DIRS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}


def parse_input(input_path: str) -> list[str]:
    with open(input_path) as input:
        return input.read().splitlines()


def add_tuples(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def main(input_path: str) -> int:
    input = parse_input(input_path)
    visited = [(0, 0)]
    head, tail = ((0, 0), (0, 0))
    for line in input:
        dir_, dist = line.split(' ')
        for _ in range(int(dist)):
            head = add_tuples(head, DIRS[dir_])
            if abs(head[0] - tail[0]) > 1:
                if head[1] - tail[1] == 1:
                    tail = add_tuples(tail, add_tuples(DIRS[dir_], DIRS['U']))
                    visited.append(tail)
                elif tail[1] - head[1] == 1:
                    tail = add_tuples(tail, add_tuples(DIRS[dir_], DIRS['D']))
                    visited.append(tail)
                else:
                    tail = add_tuples(tail, DIRS[dir_])
                    visited.append(tail)
            elif abs(head[1] - tail[1]) > 1:
                if head[0] - tail[0] == 1:
                    tail = add_tuples(tail, add_tuples(DIRS[dir_], DIRS['R']))
                    visited.append(tail)
                elif tail[0] - head[0] == 1:
                    tail = add_tuples(tail, add_tuples(DIRS[dir_], DIRS['L']))
                    visited.append(tail)
                else:
                    tail = add_tuples(tail, DIRS[dir_])
                    visited.append(tail)
    return len(set(visited))


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
