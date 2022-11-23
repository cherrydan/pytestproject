import pytest

from my_funcs.division import division


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, a, b", [(ZeroDivisionError, 10, 0),
                                                      (TypeError, "10", "5")])
def test_division_with_error(expected_exception, a, b):
    with pytest.raises(expected_exception):
        division(a, b)
