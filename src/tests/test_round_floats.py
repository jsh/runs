import pytest
from runs.runs import round_floats


@pytest.mark.parametrize(
    "floats, expected",
    [
        ([1.234, 2.345], [1.23, 2.35]),
        ([-1.234, -2.345], [-1.23, -2.35]),
        ([1.2345, 2.3456], [1.23, 2.35]),
        ([1.2, 2.3], [1.20, 2.30]),
        ([1.234, 2.345, 3.456], [1.23, 2.35, 3.46]),
        ([], []),
    ],
)
def test_round_floats(floats, expected):
    assert round_floats(floats) == expected


def test_non_float_values():
    with pytest.raises(TypeError):
        round_floats([1.2, "a", 3.4])
