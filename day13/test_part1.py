from __future__ import annotations

import pytest

from . import part1


@pytest.mark.parametrize(
    ('input_path', 'output'),

    [
        ('test_input.txt', 13),
    ],
)
def test_input(input_path, output):
    assert part1.main(input_path) == output
