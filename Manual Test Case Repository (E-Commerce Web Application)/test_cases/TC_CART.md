# Test Cases — Shopping Cart Module

**Module:** Shopping Cart
**Application:** SauceDemo (https://www.saucedemo.com)
**Total Test Cases:** 11
**Prepared By:** [QA Engineer Name]
**Last Updated:** [Date]

---

> **Precondition for all test cases in this module (unless stated otherwise):**
> User is logged in as `standard_user` with password `secret_sauce`. User is on the Products inventory page (`/inventory.html`). The cart is empty at the start of each test case.

---

## TC_CART_001 — Add Single Item to Cart

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_001 |
| **Title**        | Adding a single product from the inventory page adds it to the cart |
| **Module**       | Shopping Cart |
| **Priority**     | High |
| **Preconditions** | User is on the Products page. Cart is empty (badge not visible). |
| **Test Steps**   | 1. On the Products page, locate **"Sauce Labs Backpack"**. <br>2. Click the **"Add to cart"** button on that product card. <br>3. Observe the cart icon in the top-right of the page. <br>4. Click the cart icon to navigate to the cart page. <br>5. Observe the items listed in the cart. |
| **Test Data**    | Product: Sauce Labs Backpack |
| **Expected Result** | 1. The "Add to cart" button changes to a **"Remove"** button after clicking. <br>2. The cart icon badge displays **"1"**. <br>3. The cart page (`/cart.html`) lists exactly one item: "Sauce Labs Backpack" with the correct price ($29.99). |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | This is the primary happy-path cart test. Must pass before multi-item and checkout tests are meaningful. |

---

## TC_CART_002 — Add Multiple Items to Cart

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_002 |
| **Title**        | Adding multiple products to the cart displays all items correctly |
| **Module**       | Shopping Cart |
| **Priority**     | High |
| **Preconditions** | User is on the Products page. Cart is empty. |
| **Test Steps**   | 1. Click **"Add to cart"** on **"Sauce Labs Backpack"**. <br>2. Click **"Add to cart"** on **"Sauce Labs Bike Light"**. <br>3. Click **"Add to cart"** on **"Sauce Labs Bolt T-Shirt"**. <br>4. Observe the cart badge after each addition. <br>5. Click the cart icon to navigate to the cart page. <br>6. Verify all 3 items are listed. |
| **Test Data**    | Products: Sauce Labs Backpack, Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt |
| **Expected Result** | After adding 3 items, the cart icon badge shows **"3"**. The cart page lists all 3 products with their correct names, descriptions, quantities (1 each), and prices. Items are not duplicated. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Verify that each item has a quantity of 1 and the product details match the inventory page. |

---

## TC_CART_003 — Remove Item from Cart Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_003 |
| **Title**        | Removing an item from the cart page removes it from the cart |
| **Module**       | Shopping Cart |
| **Priority**     | High |
| **Preconditions** | User has added "Sauce Labs Backpack" and "Sauce Labs Bike Light" to the cart. User is on the cart page (`/cart.html`). Cart badge shows "2". |
| **Test Steps**   | 1. On the cart page, locate the **"Remove"** button next to **"Sauce Labs Backpack"**. <br>2. Click the **"Remove"** button. <br>3. Observe the cart contents. <br>4. Observe the cart badge in the header. |
| **Test Data**    | Item to remove: Sauce Labs Backpack |
| **Expected Result** | "Sauce Labs Backpack" is removed from the cart. The cart now shows only "Sauce Labs Bike Light". The cart badge updates to **"1"**. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Verify that removing one item does not affect the remaining item in the cart. |

---

## TC_CART_004 — Remove Item from Product Listing Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_004 |
| **Title**        | Removing an item via the "Remove" button on the product listing page updates the cart |
| **Module**       | Shopping Cart |
| **Priority**     | High |
| **Preconditions** | "Sauce Labs Bolt T-Shirt" has been added to the cart. User is on the Products page. The product card shows a "Remove" button. |
| **Test Steps**   | 1. On the Products page, locate **"Sauce Labs Bolt T-Shirt"** (which shows a "Remove" button). <br>2. Click the **"Remove"** button on that product card. <br>3. Observe the cart badge. <br>4. Navigate to the cart page and verify the item is not listed. |
| **Test Data**    | Item to remove: Sauce Labs Bolt T-Shirt |
| **Expected Result** | The "Remove" button reverts to **"Add to cart"** for that product. The cart badge count decreases by 1 (or disappears if it was the only item). The cart page does not list "Sauce Labs Bolt T-Shirt". |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | This tests the alternate (non-cart-page) removal flow. Ensures both removal mechanisms work correctly. |

---

## TC_CART_005 — Cart Badge Count Accuracy — Single Item

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_005 |
| **Title**        | Cart badge displays "1" after exactly one item is added to the cart |
| **Module**       | Shopping Cart |
| **Priority**     | Medium |
| **Preconditions** | User is on the Products page. Cart is empty (no badge visible). |
| **Test Steps**   | 1. Confirm the cart icon shows no badge (empty cart). <br>2. Click **"Add to cart"** on any one product. <br>3. Immediately observe the cart icon badge. |
| **Test Data**    | Product: Any single product |
| **Expected Result** | The cart badge appears and displays the number **"1"** immediately after the product is added. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | The badge should update without requiring a page reload. Note if there is any delay in the badge updating. |

---

## TC_CART_006 — Cart Badge Count Accuracy — All Items Added

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_006 |
| **Title**        | Cart badge accurately reflects total item count as all 6 products are added one by one |
| **Module**       | Shopping Cart |
| **Priority**     | Medium |
| **Preconditions** | User is on the Products page. Cart is empty. |
| **Test Steps**   | 1. Click **"Add to cart"** on product 1 — verify badge shows "1". <br>2. Click **"Add to cart"** on product 2 — verify badge shows "2". <br>3. Repeat for products 3, 4, 5, and 6. <br>4. After adding all 6, verify the badge shows "6". |
| **Test Data**    | All 6 products on the inventory page |
| **Expected Result** | The cart badge increments by 1 for each product added, displaying: 1 → 2 → 3 → 4 → 5 → 6. After all 6 are added, the badge shows **"6"**. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Catches off-by-one errors or badge counter synchronisation issues. |

---

## TC_CART_007 — Cart Persists After Navigating to Product Detail Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_007 |
| **Title**        | Cart contents are preserved after navigating to a product detail page and returning |
| **Module**       | Shopping Cart |
| **Priority**     | High |
| **Preconditions** | "Sauce Labs Backpack" has been added to the cart. Cart badge shows "1". User is on the Products page. |
| **Test Steps**   | 1. Confirm cart badge shows "1". <br>2. Click on the product name **"Sauce Labs Bike Light"** to navigate to its detail page. <br>3. Observe the cart badge on the detail page. <br>4. Click **"Back to products"**. <br>5. Observe the cart badge on the inventory page. <br>6. Navigate to the cart page and verify contents. |
| **Test Data**    | Pre-added item: Sauce Labs Backpack |
| **Expected Result** | The cart badge continues to display **"1"** on all pages visited. After returning to the inventory and navigating to the cart, "Sauce Labs Backpack" is still present in the cart. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Session/state persistence test. Cart contents should not be lost by navigating between pages. |

---

## TC_CART_008 — Empty Cart State Display

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_008 |
| **Title**        | Cart page shows an appropriate empty state when no items have been added |
| **Module**       | Shopping Cart |
| **Priority**     | Medium |
| **Preconditions** | User is on the Products page. Cart is empty (no items added). |
| **Test Steps**   | 1. Confirm the cart badge is not visible (empty cart). <br>2. Click the cart icon to navigate to the cart page (`/cart.html`). <br>3. Observe the cart page content. |
| **Test Data**    | Cart: empty |
| **Expected Result** | The cart page loads at `/cart.html`. No product items are listed. The page may show an empty state message or simply show the cart with zero items. The "Checkout" button is present but may be disabled, or navigating away from an empty cart should be handled gracefully. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | Note whether a "Your cart is empty" message appears. Observe the behaviour of the "Checkout" button when the cart is empty. |

---

## TC_CART_009 — Continue Shopping Button Returns to Inventory

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_009 |
| **Title**        | "Continue Shopping" button on the cart page returns user to the inventory page |
| **Module**       | Shopping Cart |
| **Priority**     | Medium |
| **Preconditions** | User is on the cart page (`/cart.html`). At least one item is in the cart. |
| **Test Steps**   | 1. Navigate to the cart page. <br>2. Locate the **"Continue Shopping"** button. <br>3. Click the **"Continue Shopping"** button. <br>4. Observe the resulting page. |
| **Test Data**    | N/A |
| **Expected Result** | User is redirected to the Products inventory page (`/inventory.html`). All products are displayed. The cart contents and badge count remain unchanged from before. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | Verify that cart state is preserved when returning to inventory via "Continue Shopping". |

---

## TC_CART_010 — Cart Items Display Correct Product Details

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_010 |
| **Title**        | Items in the cart display the correct product name, description, quantity, and price |
| **Module**       | Shopping Cart |
| **Priority**     | High |
| **Preconditions** | "Sauce Labs Fleece Jacket" has been added to the cart from the inventory page. User is on the cart page. |
| **Test Steps**   | 1. Add "Sauce Labs Fleece Jacket" to the cart from the inventory page. <br>2. Navigate to the cart page. <br>3. Observe the product row for "Sauce Labs Fleece Jacket". <br>4. Verify the product name, description snippet, quantity, and price shown. |
| **Test Data**    | Product: Sauce Labs Fleece Jacket (Price: $49.99) |
| **Expected Result** | The cart page displays: Name = "Sauce Labs Fleece Jacket", a description, Quantity = **1**, Price = **$49.99**. The displayed price matches the price shown on the inventory and detail pages. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Price accuracy is business-critical. Any discrepancy between the cart price and inventory price must be raised as a Critical bug. |

---

## TC_CART_011 — Cart Badge Disappears When All Items Are Removed

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_CART_011 |
| **Title**        | Cart badge disappears after all items are removed from the cart |
| **Module**       | Shopping Cart |
| **Priority**     | Medium |
| **Preconditions** | User has added exactly one item to the cart. Cart badge shows "1". User is on the cart page. |
| **Test Steps**   | 1. On the cart page, click **"Remove"** on the single item present. <br>2. Observe the cart page. <br>3. Observe the cart icon badge in the header. |
| **Test Data**    | Single item: Any product |
| **Expected Result** | The item is removed from the cart. The cart page shows an empty state. The cart icon badge **disappears** (is no longer visible), rather than showing "0". |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | A badge showing "0" instead of disappearing is a UI defect. Verify the badge is completely hidden, not just displaying "0". |

---

*End of TC_CART.md — 11 test cases documented.*
