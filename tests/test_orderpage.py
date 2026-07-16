import pytest
from playwright.sync_api import expect

from fromScratch.pages.home import Home
from fromScratch.pages.orders import Order


@pytest.mark.parametrize("login",[1,0],indirect=True)
def test_orderpage(login):
    home=Home(login)
    order=home.navigate_orders_page()
    #home.navigate_orders_page()
    expect(order.verify_orders_page()).to_be_visible()
    order.navigate_home_page()

