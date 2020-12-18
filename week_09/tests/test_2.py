import pytest


def test_len_1(len_of_folder):
    assert len_of_folder[0] == 100


@pytest.mark.xfail()
def test_len_2(len_of_folder):
    assert len_of_folder[1] == 3
