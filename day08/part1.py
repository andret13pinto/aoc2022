from __future__ import annotations

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


def is_tree_visible(tree: tuple[int, int], matrix: np.array) -> bool:
    # upper side
    current_pos = (tree[0] - 1, tree[1])
    while current_pos[0] >= 0:
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0] - 1, current_pos[1])
        else:
            break
    else:
        return True
    # down side
    current_pos = (tree[0] + 1, tree[1])
    while current_pos[0] < len(matrix[0]):
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0] + 1, current_pos[1])
        else:
            break
    else:
        return True
    # left side
    current_pos = (tree[0], tree[1] - 1)
    while current_pos[1] >= 0:
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0], current_pos[1] - 1)
        else:
            break
    else:
        return True
    # right side
    current_pos = (tree[0], tree[1] + 1)
    while current_pos[1] < len(matrix[0]):
        if matrix[current_pos] < matrix[tree]:
            current_pos = (current_pos[0], current_pos[1] + 1)
        else:
            break
    else:
        return True
    return False


def main(input_path: str) -> int:
    tree_matrix = parse_input(input_path)
    visible_count = 0
    for y in range(1, len(tree_matrix) - 1):
        for x in range(1, len(tree_matrix[0]) - 1):
            if is_tree_visible((y, x), tree_matrix):
                visible_count += 1
    return visible_count + 2*len(tree_matrix) + 2*len(tree_matrix[0]) - 4


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
