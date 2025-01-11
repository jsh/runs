import pytest
from runs.runs import collect_runs_count


def test_small_list_size():
    n = 2
    result = collect_runs_count(n)
    assert isinstance(result, dict)
    assert len(result) == 2  # 2 permutations with 2 elements


def test_medium_list_size():
    n = 5
    result = collect_runs_count(n)
    assert isinstance(result, dict)
    assert len(result) > 2  # more than 2 permutations with 5 elements


def test_large_list_size():
    n = 10
    result = collect_runs_count(n)
    assert isinstance(result, dict)
    assert len(result) > 2  # more than 2 permutations with 10 elements


def test_edge_case():
    n = 1
    result = collect_runs_count(n)
    assert isinstance(result, dict)
    assert len(result) == 1  # 1 permutation with 1 element


def test_invalid_input():
    with pytest.raises(ValueError):
        collect_runs_count(0)
    with pytest.raises(ValueError):
        collect_runs_count(-1)
    # with pytest.raises(TypeError):
    #    collect_runs_count(2.5)
