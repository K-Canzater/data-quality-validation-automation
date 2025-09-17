# Playwright Web UI Automation Suite

A collection of automated UI tests built with Playwright to validate critical user flows on a live e-commerce website. This project demonstrates foundational skills in test automation, including browser interaction, assertions, and setup.

## 🚀 Overview

This suite automates key smoke tests to ensure core functionality remains stable. Automating these repetitive manual checks allows for rapid feedback and frees up QA resources for more complex exploratory testing.

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

## 📁 Project Structure
├── tests/
│   ├── test_login.py
│   └── test_cart.py
├── pages/
│   ├── login_page.py
│   └── product_page.py
├── requirements.txt
└── README.md

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

## 📸 Example Output

(You can add a short GIF or screenshot of the tests running here later if you want! It's a great visual touch.)

---

## 🔮 Future Enhancements

-   Integrate with a CI/CD pipeline (e.g., GitHub Actions).
-   Add parallel execution for faster test runs.
-   Implement a Page Object Model (POM) for better maintainability.
-   Add more test cases for broader coverage.

---

💡 Developed as part of my journey to transition into an Automation-focused QA role.


