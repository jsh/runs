import pytest
from runs.runs import count_runs  # replace 'your_module' with the actual module name


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([], 0),
        ([1.0], 1),
        ([1.0, 2.0, 3.0], 1),
        ([3.0, 2.0, 1.0], 3),
        ([1.0, 2.0, 3.0, 2.0, 1.0], 2),
    ],
)
def test_count_runs(input_list, expected_output):
    assert count_runs(input_list) == expected_output
