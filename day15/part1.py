from __future__ import annotations

import sys
from collections import OrderedDict


def man_dist(point_a: tuple, point_b: tuple):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def parse_input(input_path: str, line_nr: int) -> dict:
    pos_map = OrderedDict()
    with open(input_path) as input:
        for line in input.read().splitlines():
            sensor = (int(line.split(':')[0].split('x=')[1].split(',')[0]),
                      int(line.split(':')[0].split('y=')[1].split(':')[0]))
            beacon = (int(line.split(':')[1].split('x=')[1].split(',')[0]),
                      int(line.split(':')[1].split('y=')[1]))
            pos_map[sensor] = 'S'
            pos_map[beacon] = 'B'
            beacon_dist = man_dist(sensor, beacon)
            if abs(sensor[1] - line_nr) > beacon_dist:
                continue
            cand = sensor
            for x1 in range(-beacon_dist, beacon_dist + 1):
                cand = (sensor[0] + x1, line_nr)
                if man_dist(cand, sensor) <= beacon_dist:
                    pos_map.setdefault(cand, '#')
    return pos_map


def main(input_path: str, line: int) -> int:
    pos_map = parse_input(input_path, line)
    return len([k for k, v in pos_map.items() if v == '#' and k[1] == line])


if __name__ == '__main__':
    print(main('input.txt', 2000000))
    sys.exit(0)
