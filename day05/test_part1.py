from __future__ import annotations

import part1
import pytest


@pytest.mark.parametrize(
    ('stack_input_path', 'cmd_input_path', 'output'),

    [
        ('test_stack_input.txt', 'test_commands_input.txt', 'CMZ'),
    ],
)
def test_input(stack_input_path, cmd_input_path, output):
    assert part1.main(stack_input_path, cmd_input_path) == output
