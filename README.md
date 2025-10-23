# Data Quality Validation Automation (Playwright)  

💡 *Automating validation of critical workflows to ensure data accuracy and process reliability.*  

---

## 🚀 Overview
This project demonstrates how I use **automation to validate and safeguard business‑critical processes**.  
The suite leverages Playwright (Python) to run smoke tests on an e‑commerce workflow, ensuring that login and cart functionality remain stable.  

By automating these checks, I reduce manual effort, accelerate feedback, and create a repeatable framework for **data/process validation**.  
The manual test cases that served as the foundation for this automation are included in this repository (`manual_test_cases.xlsx`).  

---

## 📋 Test Cases Automated
- **TC_LOGIN_001: Verify successful user login with valid credentials**  
  - *Actions:* Navigates to login page, enters valid username/password, submits form.  
  - *Validation:* Confirms user is redirected to the dashboard/homepage.  

- **TC_CART_001: Verify a user can add a single item to the shopping cart**  
  - *Actions:* Logs in, navigates to a product page, clicks "Add to Cart".  
  - *Validation:* Confirms cart counter updates correctly and item appears in the cart.  

---

## 🛠️ Tech Stack
- **Automation Framework:** Playwright  
- **Language:** Python  
- **Testing Framework:** Pytest  
- **Browser:** Chromium  

---

## 🏃‍♂️ Execution
Tests are implemented with **Python, Playwright, and Pytest**.  
They validate critical workflows (login, cart) and can be run locally in a standard Python environment.  

---

## 📊 What This Demonstrates
- Ability to **design manual test cases** and translate them into automated scripts.  
- Experience with **process validation and reconciliation** through automation.  
- Hands‑on use of **Python, Playwright, and Pytest** to ensure system reliability.  
- A mindset focused on **data quality, accuracy, and repeatable validation frameworks**.  

---
