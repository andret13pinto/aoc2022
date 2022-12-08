from __future__ import annotations

import math
import sys

import numpy as np


def parse_input(input_path: str) -> list[str]:
    with open(input_path) as input:
        data = input.read().splitlines()
        tree_matrix = np.zeros((len(data), len(data[0])))
        for pos_y, line in enumerate(data):
            for pos_x, char in enumerate(line.rstrip()):
                tree_matrix[pos_y, pos_x] = char
    return tree_matrix


def compute_viewing_distances(
    tree: tuple[int, int], matrix: np.array,
) -> list[int]:
    # upper side
    current_pos = (tree[0] - 1, tree[1])
    distances = [0, 0, 0, 0]
    while current_pos[0] >= 0:
        distances[0] += 1
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0] - 1, current_pos[1])
        else:
            break
    # down side
    current_pos = (tree[0] + 1, tree[1])
    while current_pos[0] < len(matrix[0]):
        distances[1] += 1
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0] + 1, current_pos[1])
        else:
            break
    # left side
    current_pos = (tree[0], tree[1] - 1)
    while current_pos[1] >= 0:
        distances[2] += 1
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0], current_pos[1] - 1)
        else:
            break
    # right side
    current_pos = (tree[0], tree[1] + 1)
    while current_pos[1] < len(matrix[0]):
        distances[3] += 1
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0], current_pos[1] + 1)
        else:
            break
    return distances


def main(input_path: str) -> int:
    tree_matrix = parse_input(input_path)
    max_score = 0
    for y in range(1, len(tree_matrix) - 1):
        for x in range(1, len(tree_matrix[0]) - 1):
            if (
                score := math.prod(
                    compute_viewing_distances(
                        (y, x), tree_matrix,
                    ),
                )
            ) > max_score:
                max_score = score
    return max_score


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
