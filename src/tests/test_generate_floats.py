import pytest
from runs.runs import generate_floats


def test_generate_floats_length():
    assert len(generate_floats(5)) == 5


def test_generate_floats_type():
    assert all(isinstance(f, float) for f in generate_floats(5))


def test_generate_floats_range():
    assert all(0 <= f <= 1 for f in generate_floats(5))


def test_generate_floats_invalid_input():
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_floats(-1)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_floats(0)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_floats(2.5)
