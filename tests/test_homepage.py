import pytest
from playwright.sync_api import expect

from fromScratch.pages.home import Home


@pytest.mark.parametrize("login",[1,0],indirect=True)
def test_homepage(login):
    home=Home(login)
    expect(home.verify_home_page()).to_be_visible()
