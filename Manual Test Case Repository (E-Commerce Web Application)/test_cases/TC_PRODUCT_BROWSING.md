# Test Cases — Product Browsing Module

**Module:** Product Browsing
**Application:** SauceDemo (https://www.saucedemo.com)
**Total Test Cases:** 12
**Prepared By:** [QA Engineer Name]
**Last Updated:** [Date]

---

> **Precondition for all test cases in this module (unless stated otherwise):**
> User is logged in as `standard_user` with password `secret_sauce` and is on the Products inventory page (`/inventory.html`).

---

## TC_BROWSE_001 — Product Listing Page Load

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_001 |
| **Title**        | Products inventory page loads fully with all 6 items visible |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User is logged in as `standard_user`. |
| **Test Steps**   | 1. Log in with `standard_user` / `secret_sauce`. <br>2. Observe the inventory page that loads at `/inventory.html`. <br>3. Count the number of product cards displayed. <br>4. Verify the page header title. |
| **Test Data**    | Username: `standard_user` / Password: `secret_sauce` |
| **Expected Result** | The Products page loads completely. Exactly **6 product cards** are visible. Each card contains a product image, name, description, price, and "Add to cart" button. The page header reads **"Products"**. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Baseline test — failure here blocks the entire browsing module. Note any missing images or broken cards. |

---

## TC_BROWSE_002 — Sort Products by Name A–Z

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_002 |
| **Title**        | Sorting products by Name (A–Z) re-orders the product list alphabetically ascending |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User is on the Products page. Products are displayed in any current order. |
| **Test Steps**   | 1. Locate the **sort dropdown** at the top-right of the product listing. <br>2. Click the dropdown. <br>3. Select **"Name (A to Z)"**. <br>4. Observe the order of the product names displayed. |
| **Test Data**    | Sort option: `Name (A to Z)` |
| **Expected Result** | Products are re-ordered alphabetically from A to Z. The first product should be **"Sauce Labs Backpack"** and sorting should proceed alphabetically through the list. No products are removed or duplicated. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Verify that all 6 products still appear after sorting. Record the actual order observed. |

---

## TC_BROWSE_003 — Sort Products by Name Z–A

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_003 |
| **Title**        | Sorting products by Name (Z–A) re-orders the product list alphabetically descending |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User is on the Products page. |
| **Test Steps**   | 1. Locate the **sort dropdown** at the top-right of the product listing. <br>2. Click the dropdown. <br>3. Select **"Name (Z to A)"**. <br>4. Observe the order of the product names displayed. |
| **Test Data**    | Sort option: `Name (Z to A)` |
| **Expected Result** | Products are re-ordered alphabetically from Z to A. The first product should be **"Test.allTheThings() T-Shirt (Red)"** and the list proceeds in reverse alphabetical order. All 6 products remain visible. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Compare result with TC_BROWSE_002 to confirm both sort directions function correctly. |

---

## TC_BROWSE_004 — Sort Products by Price Low–High

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_004 |
| **Title**        | Sorting products by Price (Low to High) orders items from cheapest to most expensive |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User is on the Products page. |
| **Test Steps**   | 1. Locate the **sort dropdown** at the top-right of the product listing. <br>2. Click the dropdown. <br>3. Select **"Price (low to high)"**. <br>4. Note the prices of items in the displayed order. |
| **Test Data**    | Sort option: `Price (low to high)` |
| **Expected Result** | Products are displayed in ascending price order. The first item should have the lowest price ($7.99 — Sauce Labs Onesie) and the last item should have the highest price ($49.99 — Sauce Labs Fleece Jacket). All 6 products remain visible. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Note the exact price of the first and last displayed items during execution to verify correct sort order. |

---

## TC_BROWSE_005 — Sort Products by Price High–Low

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_005 |
| **Title**        | Sorting products by Price (High to Low) orders items from most expensive to cheapest |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User is on the Products page. |
| **Test Steps**   | 1. Locate the **sort dropdown** at the top-right of the product listing. <br>2. Click the dropdown. <br>3. Select **"Price (high to low)"**. <br>4. Note the prices of items in the displayed order. |
| **Test Data**    | Sort option: `Price (high to low)` |
| **Expected Result** | Products are displayed in descending price order. The first item should be the most expensive ($49.99 — Sauce Labs Fleece Jacket) and the last should be the cheapest ($7.99 — Sauce Labs Onesie). All 6 products remain visible. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | This is the inverse of TC_BROWSE_004. Cross-reference to confirm both price sort directions behave correctly. |

---

## TC_BROWSE_006 — Navigate to a Product Detail Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_006 |
| **Title**        | Clicking a product name on the listing page navigates to the product detail page |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User is on the Products page with all 6 products visible. |
| **Test Steps**   | 1. Identify any product on the listing page (e.g., "Sauce Labs Backpack"). <br>2. Click on the **product name** (hyperlink text). <br>3. Observe the resulting page. |
| **Test Data**    | Product: Sauce Labs Backpack |
| **Expected Result** | The browser navigates to the individual product detail page for "Sauce Labs Backpack" (URL: `/inventory-item.html?id=4`). The detail page displays the product name, description, price, image, and an "Add to cart" button. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Critical |
| **Notes**        | Also test clicking the product image as a separate observation — note whether image click also navigates to detail page. |

---

## TC_BROWSE_007 — Product Image Navigates to Detail Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_007 |
| **Title**        | Clicking a product image on the listing page navigates to the product detail page |
| **Module**       | Product Browsing |
| **Priority**     | Medium |
| **Preconditions** | User is on the Products page with all 6 products visible. |
| **Test Steps**   | 1. Identify any product on the listing page. <br>2. Click on the **product image** (not the product name). <br>3. Observe the resulting page and URL. |
| **Test Data**    | Product: Sauce Labs Bike Light |
| **Expected Result** | The browser navigates to the product detail page for the selected item. The URL updates to reflect the selected product's detail page. The detail page is identical to that reached via the product name link. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | Complements TC_BROWSE_006. If clicking the image does not navigate, this is a usability defect. |

---

## TC_BROWSE_008 — Product Detail Page Displays Correct Information

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_008 |
| **Title**        | Product detail page displays the correct name, description, price, and image |
| **Module**       | Product Browsing |
| **Priority**     | High |
| **Preconditions** | User has navigated to the product detail page for "Sauce Labs Bolt T-Shirt". |
| **Test Steps**   | 1. From the Products page, click on **"Sauce Labs Bolt T-Shirt"**. <br>2. Verify the product name displayed on the detail page. <br>3. Verify the product description text is present and non-empty. <br>4. Verify the product price is displayed (e.g., $15.99). <br>5. Verify that a product image is displayed and loads correctly (no broken image icon). |
| **Test Data**    | Product: Sauce Labs Bolt T-Shirt |
| **Expected Result** | Detail page displays: Name = "Sauce Labs Bolt T-Shirt", Description = relevant product description text, Price = "$15.99", Image = the correct product image loaded without error. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Check that no placeholder text (e.g., "Lorem ipsum") is used in production. Verify image src is not broken. |

---

## TC_BROWSE_009 — Back Button Returns to Product Listing

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_009 |
| **Title**        | "Back to products" button on detail page navigates back to the inventory listing |
| **Module**       | Product Browsing |
| **Priority**     | Medium |
| **Preconditions** | User has navigated from the Products page to any product detail page. |
| **Test Steps**   | 1. From a product detail page, locate the **"Back to products"** button/link. <br>2. Click the **"Back to products"** button. <br>3. Observe the page that loads. |
| **Test Data**    | Any product detail page |
| **Expected Result** | User is returned to the Products inventory page (`/inventory.html`). All 6 products are still displayed. The previously viewed product is visible in the listing. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Verify that any cart items previously added are still present (cart state preserved). |

---

## TC_BROWSE_010 — Product Count Remains Consistent After Sorting

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_010 |
| **Title**        | All 6 products remain visible on the page after applying each sort option |
| **Module**       | Product Browsing |
| **Priority**     | Medium |
| **Preconditions** | User is on the Products page. |
| **Test Steps**   | 1. Note the total number of products (should be 6). <br>2. Select sort option **"Name (A to Z)"** — count products. <br>3. Select sort option **"Name (Z to A)"** — count products. <br>4. Select sort option **"Price (low to high)"** — count products. <br>5. Select sort option **"Price (high to low)"** — count products. |
| **Test Data**    | All four sort options applied sequentially |
| **Expected Result** | After each sort option is applied, exactly **6 products** are displayed. No products are added, removed, or duplicated by the sorting operation. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | This catches a potential regression where sorting could accidentally filter out results. |

---

## TC_BROWSE_011 — Product Description Visible on Inventory Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_011 |
| **Title**        | Each product card on the inventory page displays a non-empty description |
| **Module**       | Product Browsing |
| **Priority**     | Medium |
| **Preconditions** | User is on the Products page. |
| **Test Steps**   | 1. Navigate to the Products page. <br>2. For each of the 6 product cards, observe the description text below the product name. |
| **Test Data**    | All 6 products on inventory page |
| **Expected Result** | Every product card displays a non-empty, meaningful description text. No card shows empty, truncated-only, or placeholder text (e.g., "N/A" or blank space). |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Minor |
| **Notes**        | Note any descriptions that appear cut off — acceptable if truncation is intentional for layout, but full text should be accessible on the detail page. |

---

## TC_BROWSE_012 — All Product Images Load on Inventory Page

| Field            | Value |
|------------------|-------|
| **Test Case ID** | TC_BROWSE_012 |
| **Title**        | All product images on the inventory page load without errors |
| **Module**       | Product Browsing |
| **Priority**     | Medium |
| **Preconditions** | User is logged in as `standard_user` and is on the Products page. |
| **Test Steps**   | 1. Navigate to the Products page as `standard_user`. <br>2. Observe each product card's image area. <br>3. Verify that no image shows a broken image icon or blank/grey placeholder. |
| **Test Data**    | Username: `standard_user` / Password: `secret_sauce` |
| **Expected Result** | All 6 product images load and render correctly. No broken image indicators are visible. Each product shows a distinct, relevant product image. |
| **Actual Result** | [To be filled during execution] |
| **Status**       | Not Run |
| **Severity**     | Major |
| **Notes**        | Known issue: `problem_user` exhibits broken images. This test uses `standard_user` to verify the baseline behaviour. Broken images for `problem_user` should be reported separately. |

---

*End of TC_PRODUCT_BROWSING.md — 12 test cases documented.*
