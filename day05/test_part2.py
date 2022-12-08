from __future__ import annotations

import pytest

from . import part2


@pytest.mark.parametrize(
    ('stack_input_path', 'cmd_input_path', 'output'),

    [
        ('test_stack_input.txt', 'test_commands_input.txt', 'MCD'),
    ],
)
def test_input(stack_input_path, cmd_input_path, output):
    assert part2.main(stack_input_path, cmd_input_path) == output
