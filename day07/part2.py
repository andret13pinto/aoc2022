from __future__ import annotations

import itertools
import sys


class Dir:
    id_iter = itertools.count()

    def __init__(self, name: str, prev: Dir | None):
        self.id = next(Dir.id_iter)
        self.name = name
        self.prev = prev
        self.size = 0
        self.nodes: dict[Dir] = {}

    def propagate_file(self, file_size: int) -> None:
        if self.prev is not None:
            self.prev.size += file_size
            self.prev.propagate_file(file_size)


def parse_input(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines


def find_file_to_remove(file_system: dict):
    REQUIRED_SIZE = 30_000_000
    MAX_SIZE = 70_000_000
    ord_file_system = {k: v for k, v in sorted(
        file_system.items(), key=lambda item: item[1].size)}
    size_root = ord_file_system[0].size
    for item in ord_file_system.values():
        if (MAX_SIZE-size_root) + item.size >= REQUIRED_SIZE:
            return item.size


def main(input_path: str) -> int:
    lines = parse_input(input_path)
    file_system = {}
    root_dir = Dir('root', None)
    file_system[root_dir.id] = root_dir
    current_dir = root_dir
    for line in lines[1:]:
        if '$' not in line:
            if 'dir' in line:
                dir_name = line.split(' ')[1]
                new_dir = Dir(dir_name, current_dir)
                file_system[new_dir.id] = new_dir
                current_dir.nodes[dir_name] = new_dir
            else:
                file_size = line.split(' ')[0]
                file_system[current_dir.id].size += int(file_size)
                current_dir.propagate_file(int(file_size))
        elif '$ cd ..' in line:
            current_dir = file_system[current_dir.id].prev
        elif '$ cd' in line:
            current_dir = current_dir.nodes[line.split(' ')[2]]
    return find_file_to_remove(file_system)


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
