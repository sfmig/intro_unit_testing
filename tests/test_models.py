import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean
from inflammation.models import daily_min
from inflammation.models import daily_max

import pytest
from pytest import raises

def test_everything_works():
    npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))

@pytest.mark.parametrize(
    "test, expected",
    [
    ([[0, 0], [0, 0], [0, 0]], [0, 0]),
    ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(np.array(expected), daily_mean(np.array(test)))

# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
#     test_array = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(np.array([0, 0]), daily_mean(test_array))
#
# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""
#     from inflammation.models import daily_mean
#     test_array = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(np.array([3, 4]), daily_mean(test_array))


@pytest.mark.parametrize(
    "test, expected",
    [
    ([0, 0], [0]),
    ([1, 2], [2]),
    ])
def test_daily_max(test,expected):
    npt.assert_equal(np.array(expected), daily_max(np.array(test)))


@pytest.mark.parametrize(
    "test, expected",
    [
    ([0, 0], [0]),
    ([1, 2], [1]),
    ])
def test_daily_min(test,expected):
    npt.assert_equal(np.array(expected), daily_min(np.array(test)))

# def test_daily_max_integers():
#     """Test that max function works for an array of positive integers."""
#     test_array = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_equal(np.array([5,6]),daily_max(test_array))
#
#
# def test_daily_min_integers():
#     """Test that min function works for an array of positive integers."""
#     test_array = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(np.array([1, 2]), daily_min(test_array))


def test_daily_min_string():

    # if there is a typeError anywhere in this indented block (with is a context manager)
    with raises(TypeError):
        daily_min([['Cannot','min'],['string','arguments']])


def test_daily_min_too_many_inputs():
    test_array = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    # if there is a typeError anywhere in this indented block (with is a context manager)
    with raises(TypeError):
        daily_min(test_array,test_array)


def test_min_bool():
    assert daily_min([True,True,True,False]) == 0


def test_mean_bool():
    assert daily_mean([True,True,True,False]) == 0.75