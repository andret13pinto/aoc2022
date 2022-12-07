from __future__ import annotations

import part2
import pytest


@pytest.mark.parametrize(
    ('signal', 'output'),

    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
    ],
)
def test_input(signal, output):
    assert part2.main(signal) == output
