

class Order:

    def __init__(self,page):
        self.page=page
        self.orders_verify = self.page.get_by_text("You have No Orders to show at this time.")
        self.go_back_to_shop_button = self.page.get_by_role("button",name="Go Back to Shop")


    def verify_orders_page(self):
        return self.orders_verify

    def navigate_home_page(self):
        from pages.home import Home
        self.go_back_to_shop_button.click()
        return Home(self.page)


