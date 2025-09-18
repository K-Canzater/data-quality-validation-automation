from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.first_item_add_btn = "#add-to-cart-sauce-labs-backpack"
        self.cart_icon = ".shopping_cart_link"

    def add_first_item_to_cart(self):
        self.page.wait_for_selector(self.first_item_add_btn)
        self.page.click(self.first_item_add_btn)

    def click_shopping_cart(self):
        self.page.wait_for_selector(self.cart_icon)
        self.page.click(self.cart_icon)
