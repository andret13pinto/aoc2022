from __future__ import annotations

import pytest

from . import part2


@pytest.mark.parametrize(
    ('input_path', 'output'),

    [
        ('test_input.txt', 8),
    ],
)
def test_input(input_path, output):
    assert part2.main(input_path) == output
