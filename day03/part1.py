import sys
import string

def parse_inpute(input_path: str) -> list[str]:
    with open(input_path) as input:
        lines = [line.rstrip() for line in input]
    return lines

def find_repeated_item(items: str) -> str:
    comp_a = set()
    comp_b = set()
    for item in items[:int(len(items)/2)]:
        comp_a.add(item)
    for item in items[int(len(items)/2):]:
        comp_b.add(item)
    return comp_a.intersection(comp_b).pop()

def main(input_path:str) -> int:
    lines = parse_inpute(input_path)
    sum_priorities = 0
    value_dict = {letter: value + 1 for value, letter in enumerate(string.ascii_letters)}
    for sack in lines:
        item = find_repeated_item(sack)
        sum_priorities += value_dict[item]
    return sum_priorities

     


    


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
