# Test Cases — Login Module

**Module:** Login
**Application:** SauceDemo (https://www.saucedemo.com)
**Total Test Cases:** 12
**Prepared By:** [QA Engineer Name]
**Last Updated:** [Date]

---

> **Severity vs Priority Note:**
> - **Severity** = The degree of impact a defect has on the system's functionality.
> - **Priority** = The urgency with which the defect should be fixed relative to business needs.
> These two attributes are assessed independently for each test case and its associated defects.

---

## TC_LOGIN_001 — Valid Login with Standard User

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_001 |
| **Title**        | Successful login with valid standard user credentials |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | Browser is open. User is on the SauceDemo login page (https://www.saucedemo.com). User is not already logged in. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `standard_user` in the Username field. <br>3. Enter `secret_sauce` in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `standard_user` / Password: `secret_sauce` |
| **Expected Result** | User is authenticated and redirected to the Products inventory page (`/inventory.html`). The page title displays "Products". |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | This is the primary happy-path test. Must pass before other tests are valid. |

---

## TC_LOGIN_002 — Login Blocked for Locked-Out User

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_002 |
| **Title**        | Login attempt with locked_out_user account is rejected with error message |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `locked_out_user` in the Username field. <br>3. Enter `secret_sauce` in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `locked_out_user` / Password: `secret_sauce` |
| **Expected Result** | Login is refused. An error message is displayed: *"Epic sadface: Sorry, this user has been locked out."* User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Validates that the account lockout mechanism functions correctly. Error message wording should be verified exactly. |

---

## TC_LOGIN_003 — Login with Invalid Username

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_003 |
| **Title**        | Login attempt with a non-existent username displays an error |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `invalid_user_xyz` in the Username field. <br>3. Enter `secret_sauce` in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `invalid_user_xyz` / Password: `secret_sauce` |
| **Expected Result** | Login fails. Error message displayed: *"Epic sadface: Username and password do not match any user in this service."* User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Error message must not reveal whether the username or password is incorrect (security best practice). |

---

## TC_LOGIN_004 — Login with Invalid Password

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_004 |
| **Title**        | Login attempt with correct username but wrong password displays an error |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `standard_user` in the Username field. <br>3. Enter `wrong_password_123` in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `standard_user` / Password: `wrong_password_123` |
| **Expected Result** | Login fails. Error message displayed: *"Epic sadface: Username and password do not match any user in this service."* User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Confirm that the error message does not differentiate between wrong username and wrong password. |

---

## TC_LOGIN_005 — Login with Empty Username Field

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_005 |
| **Title**        | Login attempt with username field left empty shows validation error |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Leave the Username field empty. <br>3. Enter `secret_sauce` in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: (empty) / Password: `secret_sauce` |
| **Expected Result** | Login fails. Error message displayed: *"Epic sadface: Username is required."* User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Validates front-end form field validation. Verify that the error icon appears on the Username field. |

---

## TC_LOGIN_006 — Login with Empty Password Field

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_006 |
| **Title**        | Login attempt with password field left empty shows validation error |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `standard_user` in the Username field. <br>3. Leave the Password field empty. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `standard_user` / Password: (empty) |
| **Expected Result** | Login fails. Error message displayed: *"Epic sadface: Password is required."* User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Verify that the error icon appears on the Password field specifically. |

---

## TC_LOGIN_007 — Login with Both Fields Empty

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_007 |
| **Title**        | Login attempt with both username and password fields empty shows validation error |
| **Module**       | Login |
| **Priority**     | Medium |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Leave the Username field empty. <br>3. Leave the Password field empty. <br>4. Click the **Login** button. |
| **Test Data**    | Username: (empty) / Password: (empty) |
| **Expected Result** | Login fails. Error message displayed: *"Epic sadface: Username is required."* (Username validation fires first.) User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Verify the order of validation messages — Username required fires first per specification. |

---

## TC_LOGIN_008 — Login with Whitespace-Only Input

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_008 |
| **Title**        | Login attempt with whitespace-only username and password shows error |
| **Module**       | Login |
| **Priority**     | Medium |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `   ` (three spaces) in the Username field. <br>3. Enter `   ` (three spaces) in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `   ` (spaces) / Password: `   ` (spaces) |
| **Expected Result** | Login fails. An appropriate error message is displayed indicating invalid credentials. User remains on the login page. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | Boundary/edge case. Tests whether whitespace-only input is treated as empty or as a real credential. |

---

## TC_LOGIN_009 — Successful Login with Problem User

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_009 |
| **Title**        | Login with problem_user credentials succeeds and redirects to inventory |
| **Module**       | Login |
| **Priority**     | Medium |
| **Preconditions** | Browser is open. User is on the SauceDemo login page. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `problem_user` in the Username field. <br>3. Enter `secret_sauce` in the Password field. <br>4. Click the **Login** button. |
| **Test Data**    | Username: `problem_user` / Password: `secret_sauce` |
| **Expected Result** | User is authenticated and redirected to the Products page. Login itself succeeds even though the account has known downstream UI defects. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Login should succeed. Known defects with product images and sorting are expected post-login. Do not fail this TC for post-login UI defects. |

---

## TC_LOGIN_010 — Successful Logout

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_010 |
| **Title**        | Logged-in user can log out successfully via the navigation menu |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | User is logged in as `standard_user` and is on the Products page. |
| **Test Steps**   | 1. From the Products page, click the **hamburger menu** icon (☰) in the top-left corner. <br>2. Verify the sidebar navigation panel opens. <br>3. Click the **Logout** link. |
| **Test Data**    | Username: `standard_user` / Password: `secret_sauce` |
| **Expected Result** | User is logged out and redirected to the Login page (https://www.saucedemo.com). Session is terminated. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Also verify that pressing the browser Back button after logout does not return to the inventory page (session should be invalidated). |

---

## TC_LOGIN_011 — Access Inventory Page Without Login

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_011 |
| **Title**        | Unauthenticated user attempting to access inventory page directly is redirected to login |
| **Module**       | Login |
| **Priority**     | High |
| **Preconditions** | User is not logged in. No active session exists. |
| **Test Steps**   | 1. Open a new browser window or clear all cookies/session data. <br>2. Directly navigate to `https://www.saucedemo.com/inventory.html` in the address bar. |
| **Test Data**    | Direct URL: `https://www.saucedemo.com/inventory.html` |
| **Expected Result** | User is redirected to the login page. An error or informational message may be displayed, e.g., *"You can only access '/inventory.html' when you are logged in."* |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | This is a security-adjacent functional test verifying route protection / authentication guard behaviour. |

---

## TC_LOGIN_012 — Error Message Dismissal (X Button)

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_LOGIN_012 |
| **Title**        | Error message displayed after failed login can be dismissed using the X button |
| **Module**       | Login |
| **Priority**     | Low |
| **Preconditions** | User is on the login page. A failed login attempt has been made, and the error message is currently visible. |
| **Test Steps**   | 1. Navigate to https://www.saucedemo.com <br>2. Enter `invalid_user` in the Username field. <br>3. Enter `bad_pass` in the Password field. <br>4. Click **Login**. <br>5. Verify the error message is displayed. <br>6. Click the **×** (close) button on the error message banner. |
| **Test Data**    | Username: `invalid_user` / Password: `bad_pass` |
| **Expected Result** | The error message banner is dismissed and no longer visible. The login form remains on screen. The input fields retain their previous values (or are cleared per application design). |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | UI validation test. Verify that error icon indicators on fields also clear when the X button is clicked. |

---

*End of TC_LOGIN.md — 12 test cases documented.*
