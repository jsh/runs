from runs.runs import split_into_sublists


def test_empty_list():
    assert split_into_sublists([]) == []


def test_single_element_list():
    assert split_into_sublists([1.0]) == [[1.0]]


def test_increasing_numbers():
    assert split_into_sublists([1.0, 2.0, 3.0, 4.0]) == [[1.0, 2.0, 3.0, 4.0]]


def test_decreasing_numbers():
    assert split_into_sublists([4.0, 3.0, 2.0, 1.0]) == [[4.0], [3.0], [2.0], [1.0]]


def test_mixed_numbers():
    assert split_into_sublists([1.1, 2.0, 3.0, 0.9, 0.8, 2.1]) == [
        [1.1, 2.0, 3.0],
        [0.9],
        [0.8, 2.1],
    ]
