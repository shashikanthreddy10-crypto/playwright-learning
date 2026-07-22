from pages.orders import Order


class Home:

    def __init__(self,page):
        self.page = page
        self.order_page = self.page.get_by_role("button", name="Orders")

    def verify_home_page(self):
        showing_results=self.page.get_by_text("Showing 3 results")
        return showing_results

    def navigate_orders_page(self):
        self.order_page.click()
        return Order(self.page)
