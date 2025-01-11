import pytest
from runs.runs import stirling_numbers_first_kind


def test_n_zero():
    assert stirling_numbers_first_kind(0) == [1]


def test_n_one():
    assert stirling_numbers_first_kind(1) == [0, 1]


def test_n_two():
    assert stirling_numbers_first_kind(2) == [0, 1, 1]


def test_n_four():
    assert stirling_numbers_first_kind(4) == [0, 6, 11, 6, 1]


# def test_negative_n():
#    with pytest.raises(ValueError):
#        stirling_numbers_first_kind(-1)


def test_non_integer_n():
    with pytest.raises(TypeError):
        stirling_numbers_first_kind(1.5)
