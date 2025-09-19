# Playwright Web UI Automation Suite

A collection of automated UI tests built with Playwright to validate critical user flows on a live e-commerce website. This project demonstrates foundational skills in test automation, including browser interaction, assertions, and setup.

## 🚀 Overview

This suite automates key smoke tests to ensure core functionality remains stable. Automating these repetitive manual checks allows for rapid feedback and frees up QA resources for more complex exploratory testing. The manual test cases that served as the foundation for this automation are included in this repository (manual_test_cases.xlsx).

## 📋 Test Cases Automated

1.  **`TC_LOGIN_001`**: Verify successful user login with valid credentials.
    *   **Actions:** Navigates to login page, enters valid username/password, submits form.
    *   **Validation:** Asserts that the user is redirected to the dashboard or homepage upon successful login.

2.  **`TC_CART_001`**: Verify a user can add a single item to the shopping cart.
    *   **Actions:** Logs in, navigates to a product page, clicks "Add to Cart".
    *   **Validation:** Asserts that the cart counter updates correctly and the item appears in the cart.

## 🛠️ Tech Stack

*   **Automation Framework:** Playwright
*   **Language:** Python
*   **Browser:** Chromium


## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/playwright-web-ui-automation.git](https://github.com/your-username/playwright-web-ui-automation.git)
    cd playwright-web-ui-automation
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Playwright browsers:**
    ```bash
    playwright install chromium
    ```

---

## 🏃‍♂️ How to Run the Tests

-   **Run all tests:**
    ```bash
    pytest
    ```
-   **Run a specific test file:**
    ```bash
    pytest tests/test_login.py
    ```
-   **Run tests in headed mode (to see the browser):**
    ```bash
    pytest --headed
    ```

---

 
💡 This project demonstrates my hands-on ability to design manual test cases and then translate them into reliable, automated scripts—bridging the gap between manual and automation testing.


