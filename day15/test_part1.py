from __future__ import annotations

import pytest

from . import part1


@pytest.mark.parametrize(
    ('input_path', 'line', 'output'),

    [
        ('test_input.txt', 10,  26),
    ],
)
def test_input(input_path, line, output):
    assert part1.main(input_path, line) == output
