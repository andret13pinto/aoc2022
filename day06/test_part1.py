from __future__ import annotations

import pytest

from . import part1


@pytest.mark.parametrize(
    ('signal', 'output'),

    [
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    ],
)
def test_input(signal, output):
    assert part1.main(signal) == output
