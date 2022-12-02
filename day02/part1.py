import sys

def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines

def rps_engine(player: str, opp: str) -> int:
    option_lookup = {'X': 1, 'Y': 2, 'Z': 3}
    converter = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    winner_lookup = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
    opp_converted = converter[opp]
    if player == opp_converted:
        score = 3
    elif winner_lookup[player] == opp_converted:
        score = 6
    else:
        score = 0
    return score + option_lookup[player]


def calculate_rps_score(input_path : str) -> int:
    lines = parse_inpute(input_path)
    score = 0
    for line in lines:
        opp, player = line.split(' ')
        score += rps_engine(player, opp)
    return score

    


if __name__ == '__main__':
    print(calculate_rps_score('input.txt'))
    sys.exit(0)
