from playwright.sync_api import Page


class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_items = ".cart_item"
        self.item_names = ".cart_item .inventory_item_name"

    def get_items_count(self):
        self.page.wait_for_selector(self.cart_items)
        return self.page.locator(self.cart_items).count()

    def get_item_names(self):
        self.page.wait_for_selector(self.item_names)
        return self.page.locator(self.item_names).all_inner_texts()
