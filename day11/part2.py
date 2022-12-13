from __future__ import annotations

import math
import sys

op_dict = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x*x,
}


class Monkey:
    def __init__(
        self, items: list[int],  div: int,
        op: tuple[str, int], true_op: int, false_op: int,
    ) -> None:
        self.items = items
        self.op = op
        self.div = div
        self.true_op = true_op
        self.false_op = false_op
        self.inspections = 0

    def pass_items(self, monkeys: list[Monkey]) -> None:
        mul_factor = math.prod(monkey.div for monkey in monkeys)
        for item in list(self.items):
            item = op_dict[self.op[0]](item, self.op[1]) % mul_factor
            self.inspections += 1
            if item % self.div == 0:
                monkeys[self.true_op].items.append(item)
            else:
                monkeys[self.false_op].items.append(item)
        self.items.clear()


def parse_input(input_path: str) -> list[Monkey]:
    monkeys = []
    with open(input_path) as input:
        lines = input.read().splitlines()
    for line in lines:
        if line.startswith('Monkey'):
            pass
        elif 'Starting items' in line:
            items = [int(item) for item in line.split(':')[1].split(',')]
        elif 'Operation' in line:
            if line.endswith('old'):
                value = 1
                op = '**'
            else:
                value = int(line.split(' ')[-1])
                op = line.split(' ')[-2]
        elif 'Test' in line:
            div = int(line.split(' ')[-1])
        elif 'If true' in line:
            true_op = int(line.split(' ')[-1])
        elif 'If false' in line:
            false_op = int(line.split(' ')[-1])
        else:
            monkeys.append(Monkey(items, div, (op, value), true_op, false_op))
    return monkeys


def main(input_path: str) -> int:
    monkeys = parse_input(input_path)
    for n in range(10_000):
        for monkey in monkeys:
            monkey.pass_items(monkeys)
    return (
        sorted([monkey.inspections for monkey in monkeys])[-1] *
        sorted([monkey.inspections for monkey in monkeys])[-2]
    )


if __name__ == '__main__':
    print(main('input.txt'))
    sys.exit(0)
