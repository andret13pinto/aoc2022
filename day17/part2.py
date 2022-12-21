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


def find_heights(jets: cycle) -> list[int]:
    rest_rocks = [((0, -1), (1, -1), (2, -1), (3, -1),
                  (4, -1), (5, -1), (6, -1))]
    rocks = ROCKS
    heights: list[int] = [-1]
    for rock_nr, _ in cycle(enumerate(rocks)):
        if len(rest_rocks) % 1000 == 0:
            print(len(rest_rocks))
        if len(rest_rocks) == 4000:
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
                    heights.append(max_height)
                    rocks = tuple(tuple((item[0], item[1] + max_height + 1)
                                        for item in rock) for rock in ROCKS)
                    break
            else:
                rock = tuple((unit[0], unit[1] - 1) for unit in rock)
                continue
            break
    return [heights[i] - heights[i-1] for i in range(1, len(heights))]


def main(input_path: str) -> int:
    jets = iter(cycle(parse_input(input_path)))
    delta_heights = find_heights(jets)
    for size_rep in range(6, len(delta_heights)//2):
        for size_start in range(1, len(delta_heights)):
            if (size_start + size_rep > len(delta_heights) or
                    size_start + 2*size_rep > len(delta_heights)):
                break
            first = delta_heights[size_start: size_start + size_rep]
            second = delta_heights[size_start +
                                   size_rep: size_start + 2*size_rep]
            if first == second:
                height_start = sum(delta_heights[:size_start])
                height_rep = sum(first)
                nr_reps = (1_000_000_000_000 - size_start)//size_rep
                rest = (1_000_000_000_000 - size_start) % size_rep
                return nr_reps*height_rep + height_start + sum(first[:rest])


if __name__ == '__main__':
    print(main('input.txt'))
