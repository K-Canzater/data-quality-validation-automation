from playwright.sync_api import Page 

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"



    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    
    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    
    def click_login(self):
        self.page.wait_for_selector(self.login_button)
        self.page.click(self.login_button)

        
