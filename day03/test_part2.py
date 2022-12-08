from __future__ import annotations

import pytest

from . import part2


@pytest.mark.parametrize(
    ('file_path', 'output'),

    [
        ('test_input_part2_a.txt', 18),
        ('test_input_part2_b.txt', 52),
    ],
)
def test_input(file_path, output):
    assert part2.main(file_path) == output
