from __future__ import annotations

import part1
import pytest


@pytest.mark.parametrize(
    ('file_path', 'output'),

    [
        ('test_input.txt', 24000),
    ],
)
def test_input(file_path, output):
    assert part1.calculate_calories(file_path) == output
