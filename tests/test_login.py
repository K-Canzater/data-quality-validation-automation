from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_vlid_login():
    with sync_playwright() as p:

        # Launch browser with slow_mo to slow actions by 500ms
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login_page = LoginPage(page)

        # go to the website
        page.goto("https://www.saucedemo.com/")
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        page.screenshot(path="test_image.png")

        # assert I landed on the inventory page
        assert page.url == "https://www.saucedemo.com/inventory.html"
        assert page.is_visible(".inventory_list")

        browser.close()
