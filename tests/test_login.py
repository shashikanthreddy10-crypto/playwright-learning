import pytest


@pytest.mark.parametrize("login",[1,0],indirect=True)
def test_logintest(login):
    pass
