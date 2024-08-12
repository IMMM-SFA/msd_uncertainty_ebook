import pytest
from msdbook.model import sum_ints

def test_sum_ints():
    """Test to make sure `sum_ints` returns the expected value."""

    int_result = sum_ints(1, 2)

    # test equality for the output
    assert int_result == 3
