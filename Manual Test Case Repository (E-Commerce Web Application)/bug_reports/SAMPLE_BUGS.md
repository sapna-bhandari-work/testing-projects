# Sample Bug Reports — SauceDemo E-Commerce Application

**Repository:** Manual E-Commerce Testing — SauceDemo
**Application Under Test:** https://www.saucedemo.com
**Document Version:** 1.0
**Prepared By:** [QA Engineer Name]
**Test Cycle:** Cycle 1 — [Date Range]

---

> These are sample bug reports demonstrating how defects found during test execution
> should be documented using the template defined in `BUG_TEMPLATE.md`.
> Bugs below span multiple modules, severity levels, and bug types as indicated.

---

## BUG_LOGIN_001 — Field Error Icons Persist After Error Banner Is Dismissed

| Field                | Value |
|----------------------|-------|
| **Bug ID**           | BUG_LOGIN_001 |
| **Title**            | Red error icons on login input fields remain visible after the error banner is closed via the × button |
| **Module**           | Login |
| **Severity**         | Minor |
| **Priority**         | Low |
| **Bug Type**         | UI / UX |
| **Environment**      | Browser: Google Chrome 121.0 \| OS: Windows 11 \| URL: https://www.saucedemo.com |
| **Test Case Ref.**   | TC_LOGIN_012 |
| **Reported By**      | [QA Engineer Name] |
| **Date Reported**    | [YYYY-MM-DD] |
| **Status**           | New |

### Steps to Reproduce

1. Navigate to https://www.saucedemo.com.
2. Enter `invalid_user` in the Username field.
3. Enter `wrong_password` in the Password field.
4. Click the **Login** button.
5. Observe that the error message banner appears and both Username and Password fields display a red × icon.
6. Click the **×** (close) button on the error message banner to dismiss it.

### Expected Result

After the error banner is dismissed via the × button, both the banner text and the red × error icons on the Username and Password input fields should be cleared. The form should return to its default, non-error visual state.

### Actual Result

The error banner text disappears when the × button is clicked. However, the red × icons on both the Username and Password input fields remain visible. The fields continue to display the error indicator styling even though no error message is shown, creating a misleading UI state that suggests the fields are in error when nothing is actively communicating that to the user.

### Attachments

- [ ] Screenshot — `BUG_LOGIN_001_error_icons_persisting.png` *(capture after dismissing banner)*
- [ ] Screen recording — N/A
- [ ] Console log — N/A

### Additional Notes

- **Frequency:** Reproducible consistently (100% reproduction rate).
- **Workaround:** Refreshing the page or re-entering data into the fields clears the icons.
- **Impact:** Low functional impact. The application is still usable, but the inconsistent visual state represents a UX defect that could confuse users into thinking their input is invalid when they have already acknowledged the error.
- **Related test cases:** TC_LOGIN_005, TC_LOGIN_006, TC_LOGIN_007 may also exhibit this behaviour.

---

## BUG_BROWSE_001 — Product Sort Does Not Function for problem_user

| Field                | Value |
|----------------------|-------|
| **Bug ID**           | BUG_BROWSE_001 |
| **Title**            | Selecting any sort option from the dropdown does not reorder the product listing when logged in as problem_user |
| **Module**           | Product Browsing |
| **Severity**         | Major |
| **Priority**         | High |
| **Bug Type**         | Functional |
| **Environment**      | Browser: Google Chrome 121.0 \| OS: Windows 11 \| URL: https://www.saucedemo.com/inventory.html |
| **Test Case Ref.**   | TC_BROWSE_002, TC_BROWSE_003, TC_BROWSE_004, TC_BROWSE_005 |
| **Reported By**      | [QA Engineer Name] |
| **Date Reported**    | [YYYY-MM-DD] |
| **Status**           | New |

### Steps to Reproduce

1. Navigate to https://www.saucedemo.com.
2. Log in with Username: `problem_user`, Password: `secret_sauce`.
3. On the Products page, note the current order of products.
4. Click the sort dropdown in the top-right area of the product listing.
5. Select **"Name (Z to A)"** from the dropdown.
6. Observe the product listing order.
7. Repeat step 4–6 for **"Price (low to high)"** and **"Price (high to low)"**.

### Expected Result

Upon selecting any sort option, the product listing should reorder to reflect the chosen sort criterion. For example, selecting "Name (Z to A)" should display the product starting with "T" (Test.allTheThings() T-Shirt) first.

### Actual Result

After selecting any sort option from the dropdown, the product listing does **not change its order**. The sort dropdown updates its displayed label to show the selected option (e.g., "Name (Z to A)"), but the products below remain in their original, default display order. The sorting operation has no visible effect.

### Attachments

- [ ] Screenshot — `BUG_BROWSE_001_sort_before.png` *(before sort selection)*
- [ ] Screenshot — `BUG_BROWSE_001_sort_after.png` *(after sort selection — same order)*
- [ ] Screen recording — `BUG_BROWSE_001_sort_demo.gif`
- [ ] Console log — N/A

### Additional Notes

- **Frequency:** Consistently reproducible with `problem_user`. Not reproducible with `standard_user`.
- **Workaround:** None available for `problem_user`. Use `standard_user` account for sort functionality testing.
- **Impact:** This defect renders the sort feature completely non-functional for `problem_user`. Any user experiencing this account state would be unable to find products by price or alphabetical order, potentially impacting purchasing decisions.
- **Scope:** All four sort options (A–Z, Z–A, Price Low–High, Price High–Low) are affected.
- **Note:** This is a known intentional defect seeded into the `problem_user` account by SauceDemo for QA practice purposes.

---

## BUG_CHECKOUT_001 — Whitespace-Only Postal Code Bypasses Checkout Form Validation

| Field                | Value |
|----------------------|-------|
| **Bug ID**           | BUG_CHECKOUT_001 |
| **Title**            | Entering whitespace characters only in the Postal Code field allows form submission to proceed to Checkout Step 2 |
| **Module**           | Checkout |
| **Severity**         | Major |
| **Priority**         | High |
| **Bug Type**         | Boundary / Edge Case |
| **Environment**      | Browser: Google Chrome 121.0 \| OS: Windows 11 \| URL: https://www.saucedemo.com/checkout-step-one.html |
| **Test Case Ref.**   | TC_CHECKOUT_004 (extended edge case) |
| **Reported By**      | [QA Engineer Name] |
| **Date Reported**    | [YYYY-MM-DD] |
| **Status**           | New |

### Steps to Reproduce

1. Log in as `standard_user` / `secret_sauce`.
2. Add any product to the cart (e.g., Sauce Labs Backpack).
3. Navigate to the cart page and click **"Checkout"**.
4. On Checkout Step 1, enter `"Test"` in the First Name field.
5. Enter `"User"` in the Last Name field.
6. In the **Postal Code** field, enter **five consecutive space characters** (`     `).
7. Click the **"Continue"** button.

### Expected Result

The form should validate the Postal Code field for meaningful (non-whitespace) content. Since five space characters constitute an effectively empty input, the form should reject the submission and display the validation error: *"Error: Postal Code is required."* The user should remain on Checkout Step 1.

### Actual Result

The validation check does not trim or check for whitespace-only input in the Postal Code field. The form accepts the five-space string as a valid postal code and proceeds to Checkout Step 2 (order summary page). The order can then be completed with an invalid postal code, resulting in a successfully "placed" order without a real delivery address.

### Attachments

- [ ] Screenshot — `BUG_CHECKOUT_001_whitespace_input.png` *(showing spaces entered in postal code)*
- [ ] Screenshot — `BUG_CHECKOUT_001_step2_reached.png` *(showing Step 2 was reached)*
- [ ] Screen recording — N/A
- [ ] Console log — N/A

### Additional Notes

- **Frequency:** Consistently reproducible.
- **Workaround:** None from the user perspective. Server-side validation should catch this in a production system.
- **Impact:** In a production e-commerce application, this could result in orders being placed with no valid delivery postal code, causing fulfilment failures. This is a data integrity and business logic defect.
- **Variations to test:** Try with a single space, tab characters, or newline characters in the postal code field — each may exhibit the same bypass behaviour.
- **Note:** This defect class is common in web forms that validate for empty strings but do not apply `trim()` to input values before validation.

---

## BUG_BROWSE_002 — Incorrect Product Images Displayed for problem_user

| Field                | Value |
|----------------------|-------|
| **Bug ID**           | BUG_BROWSE_002 |
| **Title**            | All product images on the inventory page display the same incorrect image when logged in as problem_user |
| **Module**           | Product Browsing |
| **Severity**         | Major |
| **Priority**         | Medium |
| **Bug Type**         | UI / Functional |
| **Environment**      | Browser: Google Chrome 121.0 \| OS: Windows 11 \| URL: https://www.saucedemo.com/inventory.html |
| **Test Case Ref.**   | TC_BROWSE_012 (extended — problem_user variant) |
| **Reported By**      | [QA Engineer Name] |
| **Date Reported**    | [YYYY-MM-DD] |
| **Status**           | New |

### Steps to Reproduce

1. Navigate to https://www.saucedemo.com.
2. Log in using Username: `problem_user`, Password: `secret_sauce`.
3. On the Products page, observe the images displayed for each of the 6 product cards.
4. Compare the images shown against the expected product images (as seen when logged in as `standard_user`).

### Expected Result

Each of the 6 product cards should display a distinct, product-specific image corresponding to the product being sold. For example:
- "Sauce Labs Backpack" should show a backpack.
- "Sauce Labs Bike Light" should show a bike light.
- "Sauce Labs Bolt T-Shirt" should show a t-shirt.

### Actual Result

All 6 product cards display the **same image** — a dog/retriever image that does not correspond to any of the products listed. No product-specific images are shown. The product name, description, and price are correctly displayed, but the visual product representation is completely wrong for every item.

### Attachments

- [ ] Screenshot — `BUG_BROWSE_002_all_same_image.png` *(showing identical dog images on all 6 product cards)*
- [ ] Screenshot — `BUG_BROWSE_002_standard_user_comparison.png` *(correct images for standard_user)*
- [ ] Screen recording — N/A
- [ ] Console log — `BUG_BROWSE_002_console_log.txt` *(check for image load errors)*

### Additional Notes

- **Frequency:** Consistent for `problem_user`; not reproducible with `standard_user`.
- **Workaround:** None for `problem_user`. Switching to `standard_user` shows correct images.
- **Impact:** While `problem_user` is a seeded test account, this defect category is High severity in a production context. Incorrect product images would severely damage customer trust, could lead to wrong product purchases, and would constitute a major brand/UX failure.
- **Scope:** Affects all 6 product cards on the inventory page and also appears on individual product detail pages for `problem_user`.

---

## BUG_CART_001 — Add to Cart Button Non-Functional for Specific Products with problem_user

| Field                | Value |
|----------------------|-------|
| **Bug ID**           | BUG_CART_001 |
| **Title**            | Clicking "Add to cart" on Sauce Labs Backpack has no effect when logged in as problem_user — item is not added to the cart |
| **Module**           | Shopping Cart |
| **Severity**         | Critical |
| **Priority**         | High |
| **Bug Type**         | Functional |
| **Environment**      | Browser: Google Chrome 121.0 \| OS: Windows 11 \| URL: https://www.saucedemo.com/inventory.html |
| **Test Case Ref.**   | TC_CART_001 (problem_user variant) |
| **Reported By**      | [QA Engineer Name] |
| **Date Reported**    | [YYYY-MM-DD] |
| **Status**           | New |

### Steps to Reproduce

1. Navigate to https://www.saucedemo.com.
2. Log in using Username: `problem_user`, Password: `secret_sauce`.
3. On the Products page, locate **"Sauce Labs Backpack"**.
4. Click the **"Add to cart"** button on the Sauce Labs Backpack product card.
5. Observe the button state change and the cart badge.
6. Navigate to the cart page and observe its contents.

### Expected Result

Upon clicking "Add to cart", the button should change to a **"Remove"** button, and the cart icon badge should display **"1"**. When navigating to the cart page, "Sauce Labs Backpack" should be listed as a cart item.

### Actual Result

Clicking the "Add to cart" button on "Sauce Labs Backpack" has no visible effect. The button does **not change** to a "Remove" state. The cart badge **does not appear**. When navigating to the cart page, the cart is empty — the item was never added. No error message is displayed to inform the user that the action failed.

### Attachments

- [ ] Screenshot — `BUG_CART_001_add_to_cart_no_change.png` *(button unchanged after click)*
- [ ] Screenshot — `BUG_CART_001_empty_cart.png` *(cart page showing no items)*
- [ ] Screen recording — `BUG_CART_001_add_to_cart_failure.gif`
- [ ] Console log — `BUG_CART_001_console_errors.txt` *(expected to show JS errors)*

### Additional Notes

- **Frequency:** Consistently reproducible with `problem_user`. Not reproducible with `standard_user`.
- **Workaround:** None for `problem_user`. `standard_user` can add all products to cart successfully.
- **Impact:** This is a **Critical** functional defect in a production context. An inability to add items to the cart would completely prevent users from completing a purchase, directly impacting revenue and conversion rates.
- **Scope:** May affect additional products beyond "Sauce Labs Backpack". Further testing of all 6 products with `problem_user` is recommended to identify the full scope.
- **Additional observation:** This defect, combined with BUG_BROWSE_001 (sort failure) and BUG_BROWSE_002 (wrong images), suggests a systemic issue with the `problem_user` account configuration — likely an intentionally seeded set of defects for QA training purposes. In a production environment, these would each be filed and tracked independently.

---

*End of SAMPLE_BUGS.md — 5 bug reports documented.*

| Bug ID           | Module           | Type              | Severity | Priority | Status |
|------------------|------------------|-------------------|----------|----------|--------|
| BUG_LOGIN_001    | Login            | UI / UX           | Minor    | Low      | New    |
| BUG_BROWSE_001   | Product Browsing | Functional        | Major    | High     | New    |
| BUG_CHECKOUT_001 | Checkout         | Boundary / Edge   | Major    | High     | New    |
| BUG_BROWSE_002   | Product Browsing | UI / Functional   | Major    | Medium   | New    |
| BUG_CART_001     | Shopping Cart    | Functional        | Critical | High     | New    |
