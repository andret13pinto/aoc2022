from __future__ import annotations

import sys


def man_dist(point_a: tuple, point_b: tuple):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def get_cands_sensor(sensor: tuple, dist: int):
    cands = set()
    for i in range(-dist - 1, dist + 2):
        jj = (dist + 1) - abs(i)
        cands.add((sensor[0] + i, sensor[1] + jj))
        cands.add((sensor[0] + i, sensor[1] - jj))
    return cands


def parse_input(input_path: str) -> tuple:
    cands: set[tuple] = set()
    sensors = {}
    beacons = []
    with open(input_path) as input:
        for line in input.read().splitlines():
            sensor = (int(line.split(':')[0].split('x=')[1].split(',')[0]),
                      int(line.split(':')[0].split('y=')[1].split(':')[0]))
            beacon = (int(line.split(':')[1].split('x=')[1].split(',')[0]),
                      int(line.split(':')[1].split('y=')[1]))
            beacon_dist = man_dist(sensor, beacon)
            sensors[sensor] = beacon_dist
            beacons.append(beacon)
    for sensor, dist in sensors.items():
        new_cands = get_cands_sensor(sensor, dist)
        inter = cands.intersection(new_cands)
        while inter:
            int_cand = inter.pop()
            for sensor, dist in sensors.items():
                if man_dist(sensor, int_cand) <= dist:
                    break
            else:
                return int_cand
        else:
            cands.update(new_cands)
    raise AssertionError('Not supposed to reach')


def main(input_path: str) -> int:
    inter = parse_input(input_path)
    return inter[0] * 4_000_000 + inter[1]


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
