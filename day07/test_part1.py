from __future__ import annotations

import part1
import pytest


@pytest.mark.parametrize(
    ('input_path', 'output'),

    [
        ('test_input.txt', 95437),
    ],
)
def test_input(input_path, output):
    assert part1.main(input_path) == output
