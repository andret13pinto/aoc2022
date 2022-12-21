from __future__ import annotations

from itertools import chain, cycle

ROCKS = (
    (
        (2, 3), (3, 3), (4, 3), (5, 3),  # horizontal line
    ),
    (
        (3, 3), (2, 4), (3, 4), (4, 4), (3, 5),  # cross
    ),
    (
        (2, 3), (3, 3), (4, 3), (4, 4), (4, 5),  # L
    ),
    (
        (2, 3), (2, 4), (2, 5), (2, 6),  # vertical line
    ),
    (
        (2, 3), (3, 3), (2, 4), (3, 4),  # square
    )
)


def parse_input(input_path: str) -> tuple:
    with open(input_path) as file:
        return tuple(char for char in file.read())


def print_grid(rest_rocks: list[tuple]) -> None:
    max_y = max([y for _, y in chain(*rest_rocks)])
    output_string = ''
    for y in reversed(range(max_y + 1)):
        for x in range(0, 7):
            if (x, y) in chain(*rest_rocks):
                output_string += '#'
            else:
                output_string += '.'
        output_string += '\n'
    print(output_string)


def main(input_path: str) -> int:
    jets = iter(cycle(parse_input(input_path)))
    rest_rocks = [((0, -1), (1, -1), (2, -1), (3, -1),
                  (4, -1), (5, -1), (6, -1))]
    rocks = ROCKS
    for rock_nr, _ in cycle(enumerate(rocks)):
        if len(rest_rocks) == 2023:
            break
        rock = rocks[rock_nr]
        while True:
            # moving with jets
            jet = next(jets)
            if jet == '<':
                for unit in rock:
                    if (unit[0] == 0 or
                            (unit[0] - 1, unit[1]) in chain(*rest_rocks)):
                        break
                else:
                    rock = tuple((unit[0] - 1, unit[1])
                                 for unit in rock)
            elif jet == '>':
                for unit in rock:
                    if (unit[0] == 6
                            or (unit[0] + 1, unit[1]) in chain(*rest_rocks)):
                        break
                else:
                    rock = tuple((unit[0] + 1, unit[1])
                                 for unit in rock)
            else:
                raise AssertionError('Not expected to reach')
            # moving down
            for unit in rock:
                if (unit[0], unit[1] - 1) in chain(*rest_rocks):
                    rest_rocks.append(rock)
                    max_height = max([y for _, y in chain(*rest_rocks)])
                    rocks = tuple(tuple((item[0], item[1] + max_height + 1)
                                        for item in rock) for rock in ROCKS)
                    break
            else:
                rock = tuple((unit[0], unit[1] - 1) for unit in rock)
                continue
            break
    # print_grid(rest_rocks)
    return max([y for _, y in chain(*rest_rocks)]) + 1


if __name__ == '__main__':
    print(main('input.txt'))
