# Requirements Traceability Matrix (RTM)

**Project:** SauceDemo E-Commerce Web Application — Manual Testing
**Document Version:** 1.0
**Prepared By:** [QA Engineer Name]
**Last Updated:** [Date]

---

## Purpose

The Requirements Traceability Matrix (RTM) maps each functional requirement (expressed as a user story) to one or more test cases that verify it. This document ensures:

- Every defined requirement has at least one corresponding test case (**forward traceability**).
- Every test case can be traced back to a business requirement (**backward traceability**).
- No requirement is left untested.
- No test case exists without a business justification.

---

## Requirement ID Convention

Requirements are identified as `REQ-[MODULE]-[XX]`:
- `REQ-LOGIN-XX` — Login module requirements
- `REQ-BROWSE-XX` — Product Browsing module requirements
- `REQ-CART-XX` — Shopping Cart module requirements
- `REQ-CHECKOUT-XX` — Checkout module requirements

---

## Module 1: Login

| Req. ID       | User Story                                                                                           | Priority | Linked Test Cases                                      | Coverage Status |
|---------------|------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------|-----------------|
| REQ-LOGIN-01  | As a user, I want to log in with valid credentials so that I can access the product inventory.        | High     | TC_LOGIN_001                                           | Covered         |
| REQ-LOGIN-02  | As a user, I want to receive a clear error message when I enter incorrect credentials so that I understand why login failed. | High     | TC_LOGIN_003, TC_LOGIN_004                             | Covered         |
| REQ-LOGIN-03  | As an administrator, I want locked-out user accounts to be blocked from logging in so that unauthorised access is prevented. | High     | TC_LOGIN_002                                           | Covered         |
| REQ-LOGIN-04  | As a user, I want the login form to validate that neither field is empty before submission so that meaningless requests are not sent to the server. | High     | TC_LOGIN_005, TC_LOGIN_006, TC_LOGIN_007, TC_LOGIN_008 | Covered         |
| REQ-LOGIN-05  | As a user, I want to log out of the application so that my session is securely terminated.            | High     | TC_LOGIN_010                                           | Covered         |
| REQ-LOGIN-06  | As a system, I want unauthenticated users who attempt to access protected pages directly to be redirected to the login page. | High     | TC_LOGIN_011                                           | Covered         |

---

## Module 2: Product Browsing

| Req. ID        | User Story                                                                                           | Priority | Linked Test Cases                                         | Coverage Status |
|----------------|------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------|-----------------|
| REQ-BROWSE-01  | As a user, I want to see all available products on the inventory page so that I can browse what is for sale. | High     | TC_BROWSE_001, TC_BROWSE_010, TC_BROWSE_011, TC_BROWSE_012 | Covered         |
| REQ-BROWSE-02  | As a user, I want to sort products by name (A–Z and Z–A) so that I can find items alphabetically.    | High     | TC_BROWSE_002, TC_BROWSE_003, TC_BROWSE_010               | Covered         |
| REQ-BROWSE-03  | As a user, I want to sort products by price (low to high and high to low) so that I can find items within my budget. | High     | TC_BROWSE_004, TC_BROWSE_005, TC_BROWSE_010               | Covered         |
| REQ-BROWSE-04  | As a user, I want to click on a product to view its full details (name, description, price, and image) on a dedicated page. | High     | TC_BROWSE_006, TC_BROWSE_007, TC_BROWSE_008               | Covered         |
| REQ-BROWSE-05  | As a user, I want to navigate back to the product listing from a product detail page so that I can continue browsing. | Medium   | TC_BROWSE_009                                             | Covered         |

---

## Module 3: Shopping Cart

| Req. ID      | User Story                                                                                           | Priority | Linked Test Cases                                | Coverage Status |
|--------------|------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------|-----------------|
| REQ-CART-01  | As a user, I want to add products to my cart so that I can collect items I wish to purchase.          | High     | TC_CART_001, TC_CART_002                         | Covered         |
| REQ-CART-02  | As a user, I want to remove items from my cart so that I can change my mind before purchasing.        | High     | TC_CART_003, TC_CART_004                         | Covered         |
| REQ-CART-03  | As a user, I want the cart icon to display a count of items in my cart so that I always know how many items I have selected. | Medium   | TC_CART_005, TC_CART_006, TC_CART_011            | Covered         |
| REQ-CART-04  | As a user, I want my cart contents to persist as I navigate between pages so that I do not lose my selections. | High     | TC_CART_007                                      | Covered         |
| REQ-CART-05  | As a user, I want to view the details (name, price, quantity) of items in my cart before proceeding to checkout. | High     | TC_CART_010                                      | Covered         |
| REQ-CART-06  | As a user, I want the ability to continue shopping from the cart page so that I can add more items before checking out. | Medium   | TC_CART_009                                      | Covered         |

---

## Module 4: Checkout

| Req. ID          | User Story                                                                                           | Priority | Linked Test Cases                                     | Coverage Status |
|------------------|------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------|-----------------|
| REQ-CHECKOUT-01  | As a user, I want to enter my shipping information (first name, last name, postal code) to proceed with checkout. | High     | TC_CHECKOUT_001, TC_CHECKOUT_006, TC_CHECKOUT_011     | Covered         |
| REQ-CHECKOUT-02  | As a user, I want the checkout form to validate required fields so that I cannot submit an incomplete order. | High     | TC_CHECKOUT_002, TC_CHECKOUT_003, TC_CHECKOUT_004, TC_CHECKOUT_005 | Covered |
| REQ-CHECKOUT-03  | As a user, I want to review my order summary (items, subtotal, tax, total) before confirming my purchase. | High     | TC_CHECKOUT_006, TC_CHECKOUT_011                      | Covered         |
| REQ-CHECKOUT-04  | As a user, I want to receive an order confirmation page after successfully completing my purchase.    | High     | TC_CHECKOUT_007                                       | Covered         |
| REQ-CHECKOUT-05  | As a user, I want to be returned to the home/inventory page after completing my order.                | Medium   | TC_CHECKOUT_008                                       | Covered         |
| REQ-CHECKOUT-06  | As a user, I want to be able to cancel my checkout at any step and return without losing my cart.     | Medium   | TC_CHECKOUT_009, TC_CHECKOUT_010                      | Covered         |

---

## Full Traceability Summary

| Req. ID          | Module           | Linked Test Cases (count) | Coverage Status |
|------------------|------------------|---------------------------|-----------------|
| REQ-LOGIN-01     | Login            | 1                         | Covered         |
| REQ-LOGIN-02     | Login            | 2                         | Covered         |
| REQ-LOGIN-03     | Login            | 1                         | Covered         |
| REQ-LOGIN-04     | Login            | 4                         | Covered         |
| REQ-LOGIN-05     | Login            | 1                         | Covered         |
| REQ-LOGIN-06     | Login            | 1                         | Covered         |
| REQ-BROWSE-01    | Product Browsing | 4                         | Covered         |
| REQ-BROWSE-02    | Product Browsing | 3                         | Covered         |
| REQ-BROWSE-03    | Product Browsing | 3                         | Covered         |
| REQ-BROWSE-04    | Product Browsing | 3                         | Covered         |
| REQ-BROWSE-05    | Product Browsing | 1                         | Covered         |
| REQ-CART-01      | Shopping Cart    | 2                         | Covered         |
| REQ-CART-02      | Shopping Cart    | 2                         | Covered         |
| REQ-CART-03      | Shopping Cart    | 3                         | Covered         |
| REQ-CART-04      | Shopping Cart    | 1                         | Covered         |
| REQ-CART-05      | Shopping Cart    | 1                         | Covered         |
| REQ-CART-06      | Shopping Cart    | 1                         | Covered         |
| REQ-CHECKOUT-01  | Checkout         | 3                         | Covered         |
| REQ-CHECKOUT-02  | Checkout         | 4                         | Covered         |
| REQ-CHECKOUT-03  | Checkout         | 2                         | Covered         |
| REQ-CHECKOUT-04  | Checkout         | 1                         | Covered         |
| REQ-CHECKOUT-05  | Checkout         | 1                         | Covered         |
| REQ-CHECKOUT-06  | Checkout         | 2                         | Covered         |
| **Totals**       | 4 modules        | 22 requirements           | **100% Covered**|

---

## Reverse Traceability — Test Cases to Requirements

| Test Case ID      | Requirement(s) Covered          |
|-------------------|---------------------------------|
| TC_LOGIN_001      | REQ-LOGIN-01                    |
| TC_LOGIN_002      | REQ-LOGIN-03                    |
| TC_LOGIN_003      | REQ-LOGIN-02                    |
| TC_LOGIN_004      | REQ-LOGIN-02                    |
| TC_LOGIN_005      | REQ-LOGIN-04                    |
| TC_LOGIN_006      | REQ-LOGIN-04                    |
| TC_LOGIN_007      | REQ-LOGIN-04                    |
| TC_LOGIN_008      | REQ-LOGIN-04                    |
| TC_LOGIN_009      | REQ-LOGIN-01                    |
| TC_LOGIN_010      | REQ-LOGIN-05                    |
| TC_LOGIN_011      | REQ-LOGIN-06                    |
| TC_LOGIN_012      | REQ-LOGIN-02 (error UI)         |
| TC_BROWSE_001     | REQ-BROWSE-01                   |
| TC_BROWSE_002     | REQ-BROWSE-02                   |
| TC_BROWSE_003     | REQ-BROWSE-02                   |
| TC_BROWSE_004     | REQ-BROWSE-03                   |
| TC_BROWSE_005     | REQ-BROWSE-03                   |
| TC_BROWSE_006     | REQ-BROWSE-04                   |
| TC_BROWSE_007     | REQ-BROWSE-04                   |
| TC_BROWSE_008     | REQ-BROWSE-04                   |
| TC_BROWSE_009     | REQ-BROWSE-05                   |
| TC_BROWSE_010     | REQ-BROWSE-02, REQ-BROWSE-03    |
| TC_BROWSE_011     | REQ-BROWSE-01                   |
| TC_BROWSE_012     | REQ-BROWSE-01                   |
| TC_CART_001       | REQ-CART-01                     |
| TC_CART_002       | REQ-CART-01                     |
| TC_CART_003       | REQ-CART-02                     |
| TC_CART_004       | REQ-CART-02                     |
| TC_CART_005       | REQ-CART-03                     |
| TC_CART_006       | REQ-CART-03                     |
| TC_CART_007       | REQ-CART-04                     |
| TC_CART_008       | REQ-CART-01 (empty state)       |
| TC_CART_009       | REQ-CART-06                     |
| TC_CART_010       | REQ-CART-05                     |
| TC_CART_011       | REQ-CART-03                     |
| TC_CHECKOUT_001   | REQ-CHECKOUT-01                 |
| TC_CHECKOUT_002   | REQ-CHECKOUT-02                 |
| TC_CHECKOUT_003   | REQ-CHECKOUT-02                 |
| TC_CHECKOUT_004   | REQ-CHECKOUT-02                 |
| TC_CHECKOUT_005   | REQ-CHECKOUT-02                 |
| TC_CHECKOUT_006   | REQ-CHECKOUT-03                 |
| TC_CHECKOUT_007   | REQ-CHECKOUT-04                 |
| TC_CHECKOUT_008   | REQ-CHECKOUT-05                 |
| TC_CHECKOUT_009   | REQ-CHECKOUT-06                 |
| TC_CHECKOUT_010   | REQ-CHECKOUT-06                 |
| TC_CHECKOUT_011   | REQ-CHECKOUT-01, REQ-CHECKOUT-03|

---

*End of rtm.md — Requirements Traceability Matrix*
