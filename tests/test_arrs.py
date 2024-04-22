import pytest

from utils import arrs
@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]


def test_get():
    assert arrs.get([], 0, "test") == "test"


def test_get_fixture(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get(array_fixture, 3, "test") == 4


def test_slice():
      assert arrs.my_slice([], None, None) == []


def test_slice_fixture(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 2) == [2]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(array_fixture, None, 4) == [1, 2, 3, 4]
