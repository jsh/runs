import pytest
from collections import Counter
from runs.runs import weighted_average  # assuming the function is in runs.runs module


def test_empty_counter():
    counter = Counter()
    with pytest.raises(ZeroDivisionError):
        weighted_average(counter)


def test_single_element():
    counter = Counter({1: 1})
    assert weighted_average(counter) == 1


def test_multiple_elements():
    counter = Counter({1: 2, 2: 3, 3: 1})
    assert weighted_average(counter) == (2 * 1 + 3 * 2 + 1 * 3) / 6


# def test_zero_values():
#    counter = Counter({1: 0, 2: 0, 3: 0})
#    assert weighted_average(counter) == 0


def test_non_integer_keys():
    counter = Counter({"a": 1, "b": 2})
    with pytest.raises(TypeError):
        weighted_average(counter)


def test_non_integer_values():
    counter = Counter({1: 1.5, 2: 2})
    assert weighted_average(counter) == (1 * 1.5 + 2 * 2) / 3.5


def test_large_numbers():
    counter = Counter({1000000: 1000000, 2000000: 2000000})
    assert weighted_average(counter) == (1000000 * 1000000 + 2000000 * 2000000) / (
        1000000 + 2000000
    )
