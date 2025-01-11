import pytest
import sys
from runs.runs import list_length


@pytest.fixture
def reset_sys_argv():
    original_argv = sys.argv
    yield
    sys.argv = original_argv


def test_valid_integer_argument(reset_sys_argv):
    sys.argv = ["script.py", "5"]
    assert list_length() == 5


def test_non_integer_argument(reset_sys_argv):
    sys.argv = ["script.py", "abc"]
    assert list_length() == 10


def test_no_arguments(reset_sys_argv):
    sys.argv = ["script.py"]
    assert list_length() == 10


def test_multiple_arguments(reset_sys_argv):
    sys.argv = ["script.py", "5", "10"]
    assert list_length() == 5
