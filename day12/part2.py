from __future__ import annotations

import heapq
import sys


def parse_input(input_path: str) -> tuple[dict, list, tuple]:
    pos_dict: dict = {}
    starts = []
    with open(input_path) as input:
        for y, line in enumerate(input.read().splitlines()):
            for x, value in enumerate(line):
                pos_dict[(x, y)] = value
                if value == 'S' or value == 'a':
                    starts.append((x, y))
                elif value == 'E':
                    end = (x, y)
    return pos_dict, starts, end


def find_candidates(coords: tuple) -> list:
    cands = []
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cands.append((coords[0] + x, coords[1] + y))
    return cands


def main(input_path: str) -> int:
    pos_dict, starts, end = parse_input(input_path)
    min_path = 10000
    for start in starts:
        queue = [(0, start)]
        help_dict = {'S': chr(ord('a') - 1), 'E': chr(ord('z') + 1)}
        visited = set()
        while queue:
            steps, pos = heapq.heappop(queue)
            if pos in visited:
                continue
            elif pos == end:
                if steps < min_path:
                    min_path = steps
            else:
                visited.add(pos)
            for cand in find_candidates(pos):
                if cand in pos_dict:
                    current_h = help_dict.get(pos_dict[pos], pos_dict[pos])
                    cand_h = help_dict.get(pos_dict[cand], pos_dict[cand])
                    if ord(cand_h) - ord(current_h) <= 1:
                        heapq.heappush(queue, (steps + 1, cand))
    return min_path


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
