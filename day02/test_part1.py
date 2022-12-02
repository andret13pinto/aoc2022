import pytest
import part1

@pytest.mark.parametrize(
    ('file_path', 'output'),

    [
        ('test_input.txt', 15)
    ]
)
def test_input(file_path, output):
    assert part1.calculate_rps_score(file_path) == output



