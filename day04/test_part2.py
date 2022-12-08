from __future__ import annotations

import pytest

from . import part2


@pytest.mark.parametrize(
    ('file_path', 'output'),

    [
        ('test_input.txt', 4),
    ],
)
def test_input(file_path, output):
    assert part2.main(file_path) == output
