from runs.runs import count_sublists


def test_empty_list():
    assert count_sublists([]) == 0


def test_single_sublist():
    assert count_sublists([[1.0]]) == 1


def test_multiple_sublists():
    assert count_sublists([[1.0], [2.0], [3.0]]) == 3


def test_sublists_with_varying_lengths():
    assert count_sublists([[1.0], [2.0, 3.0], [4.0, 5.0, 6.0]]) == 3
