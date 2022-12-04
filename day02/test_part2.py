from __future__ import annotations

import part2
import pytest


@pytest.mark.parametrize(
    ('file_path', 'output'),

    [
        ('test_input.txt', 12),
    ],
)
def test_input(file_path, output):
    assert part2.calculate_rps_score(file_path) == output
