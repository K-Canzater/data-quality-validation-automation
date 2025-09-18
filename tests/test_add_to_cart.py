from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_single_item_to_cart():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Go to the website
        page.goto("https://www.saucedemo.com/")

        # 1️⃣ Log in
        login_page = LoginPage(page)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # 2️⃣ Add first item to cart
        inventory_page = InventoryPage(page)
        inventory_page.add_first_item_to_cart()

        # 3️⃣ Check cart badge
        badge_text = page.inner_text(".shopping_cart_badge")
        assert badge_text == "1"

        # 4️⃣ Go to cart page
        inventory_page.click_shopping_cart()
        page.screenshot(path="cart_page.png")

        # 5️⃣ Check cart has correct item
        cart_page = CartPage(page)
        assert cart_page.get_items_count() == 1
        assert "Sauce Labs Backpack" in cart_page.get_item_names()

        browser.close()
