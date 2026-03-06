# Test Cases — Checkout Module

**Module:** Checkout
**Application:** SauceDemo (https://www.saucedemo.com)
**Total Test Cases:** 11
**Prepared By:** [QA Engineer Name]
**Last Updated:** [Date]

---

> **Precondition for all test cases in this module (unless stated otherwise):**
> User is logged in as `standard_user` with password `secret_sauce`. At least one item has been added to the cart. User has navigated to the cart page (`/cart.html`).

---

## TC_CHECKOUT_001 — Full Checkout Flow with Valid Data

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_001 |
| **Title**        | Complete end-to-end checkout with valid customer information and confirm order |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | "Sauce Labs Backpack" is in the cart. User is on the cart page. |
| **Test Steps**   | 1. On the cart page, click the **"Checkout"** button. <br>2. On the Checkout Step 1 page (`/checkout-step-one.html`), enter **"Test"** in First Name. <br>3. Enter **"User"** in Last Name. <br>4. Enter **"12345"** in Postal Code / ZIP. <br>5. Click the **"Continue"** button. <br>6. On the Checkout Step 2 page (`/checkout-step-two.html`), review the order summary. <br>7. Click the **"Finish"** button. <br>8. Observe the confirmation page. |
| **Test Data**    | First Name: `Test` / Last Name: `User` / Postal Code: `12345` |
| **Expected Result** | Step 1 → Step 2 navigation succeeds. Step 2 shows order summary with correct items and total. After clicking "Finish", the order confirmation page (`/checkout-complete.html`) loads, displaying a success message (e.g., "Thank you for your order!"). |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | This is the primary checkout happy-path. Failure here is a Critical defect. Capture the confirmation header text exactly. |

---

## TC_CHECKOUT_002 — Checkout with Empty First Name

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_002 |
| **Title**        | Checkout form submission with empty First Name field shows validation error |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | At least one item is in the cart. User has clicked "Checkout" and is on the Checkout Step 1 page. |
| **Test Steps**   | 1. Leave the **First Name** field empty. <br>2. Enter `"User"` in the Last Name field. <br>3. Enter `"12345"` in the Postal Code field. <br>4. Click the **"Continue"** button. |
| **Test Data**    | First Name: (empty) / Last Name: `User` / Postal Code: `12345` |
| **Expected Result** | Form submission is blocked. An error message is displayed: *"Error: First Name is required"*. User remains on Checkout Step 1. No navigation to Step 2 occurs. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Verify the exact wording of the error message. Check that an error icon appears on the First Name field. |

---

## TC_CHECKOUT_003 — Checkout with Empty Last Name

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_003 |
| **Title**        | Checkout form submission with empty Last Name field shows validation error |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | At least one item is in the cart. User is on the Checkout Step 1 page. |
| **Test Steps**   | 1. Enter `"Test"` in the First Name field. <br>2. Leave the **Last Name** field empty. <br>3. Enter `"12345"` in the Postal Code field. <br>4. Click the **"Continue"** button. |
| **Test Data**    | First Name: `Test` / Last Name: (empty) / Postal Code: `12345` |
| **Expected Result** | Form submission is blocked. An error message is displayed: *"Error: Last Name is required"*. User remains on Checkout Step 1. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Confirm the error specifically mentions Last Name, not a generic "field required" message. |

---

## TC_CHECKOUT_004 — Checkout with Empty Postal Code

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_004 |
| **Title**        | Checkout form submission with empty Postal Code field shows validation error |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | At least one item is in the cart. User is on the Checkout Step 1 page. |
| **Test Steps**   | 1. Enter `"Test"` in the First Name field. <br>2. Enter `"User"` in the Last Name field. <br>3. Leave the **Postal Code** field empty. <br>4. Click the **"Continue"** button. |
| **Test Data**    | First Name: `Test` / Last Name: `User` / Postal Code: (empty) |
| **Expected Result** | Form submission is blocked. An error message is displayed: *"Error: Postal Code is required"*. User remains on Checkout Step 1. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Note any difference in error icon rendering between this test and TC_CHECKOUT_002/003. |

---

## TC_CHECKOUT_005 — Checkout with All Fields Empty

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_005 |
| **Title**        | Checkout form submission with all three fields empty shows First Name validation error |
| **Module**       | Checkout |
| **Priority**     | Medium |
| **Preconditions** | At least one item is in the cart. User is on the Checkout Step 1 page. |
| **Test Steps**   | 1. Leave **First Name**, **Last Name**, and **Postal Code** fields all empty. <br>2. Click the **"Continue"** button. |
| **Test Data**    | First Name: (empty) / Last Name: (empty) / Postal Code: (empty) |
| **Expected Result** | Form submission is blocked. The first validation error fires: *"Error: First Name is required"*. User remains on Checkout Step 1. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Confirms validation priority order (First Name checked first). Compare with TC_CHECKOUT_002. |

---

## TC_CHECKOUT_006 — Order Summary Displays Correct Items and Prices

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_006 |
| **Title**        | Checkout Step 2 order summary displays the correct item(s), subtotal, tax, and total |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | "Sauce Labs Bike Light" ($9.99) has been added to the cart. User has completed Checkout Step 1 with valid data and is on the Checkout Step 2 page. |
| **Test Steps**   | 1. Add "Sauce Labs Bike Light" to cart and proceed through Checkout Step 1 with valid data. <br>2. On Checkout Step 2, verify the listed item name and price. <br>3. Verify the "Item total" subtotal. <br>4. Verify the "Tax" amount. <br>5. Verify the "Total" amount equals Item total + Tax. |
| **Test Data**    | Product: Sauce Labs Bike Light (Price: $9.99) |
| **Expected Result** | Step 2 displays: Item = "Sauce Labs Bike Light", Price = $9.99, Item total = $9.99, Tax = $0.80, Total = $10.79. The total equals the sum of item total and tax. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Record exact values shown for Item total, Tax, and Total during execution. Any arithmetic discrepancy is a Critical defect. Tax rate appears to be ~8%. |

---

## TC_CHECKOUT_007 — Order Confirmation Page Content

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_007 |
| **Title**        | Order confirmation page displays a success header, confirmation text, and a back home link |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | User has completed the full checkout flow (valid data entered, items in cart, "Finish" clicked). User is on the checkout complete page (`/checkout-complete.html`). |
| **Test Steps**   | 1. Complete the full checkout flow (as per TC_CHECKOUT_001). <br>2. On the confirmation page, verify the main heading. <br>3. Verify the confirmation sub-text. <br>4. Verify a confirmation image (checkmark/pony express) is visible. <br>5. Verify a **"Back Home"** button is present. |
| **Test Data**    | N/A (result of completed order) |
| **Expected Result** | Confirmation page displays: Heading = **"Thank you for your order!"**, Subtext = "Your order has been dispatched...", A checkmark/pony express image, and a **"Back Home"** button. URL is `/checkout-complete.html`. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Record the exact heading and subtext wording shown. Any missing element on the confirmation page should be logged as a defect. |

---

## TC_CHECKOUT_008 — Back Home Button Returns to Inventory After Order

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_008 |
| **Title**        | "Back Home" button on the order confirmation page returns user to the inventory page |
| **Module**       | Checkout |
| **Priority**     | Medium |
| **Preconditions** | User has completed checkout and is on the order confirmation page (`/checkout-complete.html`). |
| **Test Steps**   | 1. On the confirmation page, locate and click the **"Back Home"** button. <br>2. Observe the resulting page and URL. <br>3. Verify the cart badge state. |
| **Test Data**    | N/A |
| **Expected Result** | User is redirected to the Products inventory page (`/inventory.html`). The cart is **empty** (badge not visible) as the order has been completed. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Confirm that the cart is cleared after a successful order — items from the completed order should not persist in the cart. |

---

## TC_CHECKOUT_009 — Cancel Checkout Step 1 Returns to Cart

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_009 |
| **Title**        | Clicking "Cancel" on Checkout Step 1 returns user to the cart without data loss |
| **Module**       | Checkout |
| **Priority**     | Medium |
| **Preconditions** | Items are in the cart. User has clicked "Checkout" and is on the Checkout Step 1 page. No information has been entered in the form. |
| **Test Steps**   | 1. On Checkout Step 1, locate the **"Cancel"** button. <br>2. Click **"Cancel"**. <br>3. Observe the resulting page. <br>4. Verify the cart contents. |
| **Test Data**    | N/A |
| **Expected Result** | User is returned to the cart page (`/cart.html`). All previously added items remain in the cart, unchanged. The cart badge count is unchanged. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Validates that cancelling checkout does not alter or clear the cart. |

---

## TC_CHECKOUT_010 — Cancel Checkout Step 2 Returns to Inventory

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_010 |
| **Title**        | Clicking "Cancel" on Checkout Step 2 returns user to the inventory page |
| **Module**       | Checkout |
| **Priority**     | Medium |
| **Preconditions** | User has completed Checkout Step 1 with valid data and is on the Checkout Step 2 (order summary) page. |
| **Test Steps**   | 1. On the Checkout Step 2 page, locate the **"Cancel"** button. <br>2. Click **"Cancel"**. <br>3. Observe the resulting page. <br>4. Verify the cart badge count. |
| **Test Data**    | N/A |
| **Expected Result** | User is returned to the Products inventory page (`/inventory.html`). Cart badge still reflects the items that were in the cart before checkout was initiated (items are not removed). |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Note: SauceDemo may redirect to inventory on Cancel from Step 2. Verify that items remain in cart. This differs from TC_CHECKOUT_009 which tests Cancel on Step 1. |

---

## TC_CHECKOUT_011 — Checkout with Multiple Items Shows Correct Total

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CHECKOUT_011 |
| **Title**        | Checkout order summary calculates correct totals when multiple items are in the cart |
| **Module**       | Checkout |
| **Priority**     | High |
| **Preconditions** | "Sauce Labs Backpack" ($29.99) and "Sauce Labs Bike Light" ($9.99) have been added to the cart. User has completed Checkout Step 1 and is on Checkout Step 2. |
| **Test Steps**   | 1. Add "Sauce Labs Backpack" and "Sauce Labs Bike Light" to the cart. <br>2. Navigate through Checkout Step 1 with valid data. <br>3. On Checkout Step 2, verify both items are listed. <br>4. Verify the Item total. <br>5. Verify the Tax amount. <br>6. Verify the Total. |
| **Test Data**    | Products: Sauce Labs Backpack ($29.99) + Sauce Labs Bike Light ($9.99) = Subtotal $39.98 |
| **Expected Result** | Both items are listed. Item total = **$39.98**. Tax = **$3.20** (approx. 8%). Total = **$43.18**. The displayed total is the arithmetic sum of item total and tax. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Record exact values during execution. Multi-item total accuracy is business-critical. |

---

*End of TC_CHECKOUT.md — 11 test cases documented.*
