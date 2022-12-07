from __future__ import annotations

import part2
import pytest


@pytest.mark.parametrize(
    ('input_path', 'output'),

    [
        ('test_input.txt', 24933642),
    ],
)
def test_input(input_path, output):
    assert part2.main(input_path) == output
