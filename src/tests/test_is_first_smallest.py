from runs.runs import is_first_smallest


def test_single_element():
    assert is_first_smallest([1.0])


def test_first_smallest():
    assert is_first_smallest([1.0, 2.0, 3.0])


def test_not_first_smallest():
    assert not is_first_smallest([2.0, 1.0, 3.0])


def test_duplicate_smallest():
    assert is_first_smallest([1.0, 1.0, 2.0])


def test_negative_numbers():
    assert is_first_smallest([-1.0, 0.0, 1.0])


def test_large_numbers():
    assert is_first_smallest([1e10, 2e10, 3e10])
