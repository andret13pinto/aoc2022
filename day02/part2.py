from __future__ import annotations

import sys

converter = {'A': 'X', 'B': 'Y', 'C': 'Z'}
winner_lookup = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}


def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines


def rps_engine(player: str, opp: str) -> int:
    option_lookup = {'X': 1, 'Y': 2, 'Z': 3}
    if player == opp:
        score = 3
    elif winner_lookup[player] == opp:
        score = 6
    else:
        score = 0
    return score + option_lookup[player]


def find_play(opp: str, outcome: str) -> str:
    if outcome == 'Y':
        return opp
    elif outcome == 'X':
        return winner_lookup[opp]
    else:
        return [
            winner for winner,
            loser in winner_lookup.items()
            if loser == opp
        ][0]


def calculate_rps_score(input_path: str) -> int:
    lines = parse_inpute(input_path)
    score = 0
    for line in lines:
        opp, outcome = line.split(' ')
        opp_converted = converter[opp]
        player = find_play(opp_converted, outcome)
        score += rps_engine(player, opp_converted)
    return score


if __name__ == '__main__':
    print(calculate_rps_score('input.txt'))
    sys.exit(0)
