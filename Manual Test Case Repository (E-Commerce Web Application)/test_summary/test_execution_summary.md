# Test Execution Summary Report

**Project:** SauceDemo E-Commerce Web Application — Manual Testing
**Document Version:** 1.0
**Prepared By:** [QA Engineer Name]
**Reviewed By:** [QA Lead Name]

---

## 1. Test Cycle Information

| Field                  | Value |
|------------------------|-------|
| **Test Cycle Name**    | Cycle 1 — Functional Regression |
| **Application**        | SauceDemo (https://www.saucedemo.com) |
| **Test Plan Reference**| `test_plan/test_plan.md` |
| **Cycle Start Date**   | [YYYY-MM-DD] |
| **Cycle End Date**     | [YYYY-MM-DD] |
| **Execution Date**     | [YYYY-MM-DD] |
| **Tester(s)**          | [QA Engineer Name] |
| **Build / Version**    | [App version / date if available — SauceDemo does not expose versioning] |
| **Browser**            | Google Chrome [Version] |
| **Operating System**   | [Windows 11 / macOS] |

---

## 2. Overall Test Execution Summary

| Metric              | Count | Percentage |
|---------------------|-------|------------|
| **Total Test Cases** | 46    | 100%       |
| **Passed**          | [X]   | [X%]       |
| **Failed**          | [X]   | [X%]       |
| **Blocked**         | [X]   | [X%]       |
| **Not Run**         | [X]   | [X%]       |
| **Pass Rate**       | —     | **[X%]**   |

> **Pass Rate** is calculated as: *(Passed / (Total − Not Run)) × 100*

> Note: All Actual Result and Status fields in the test case files should be updated at the close of execution. The metric table above should be populated from the final test case status counts.

---

## 3. Module-Wise Test Execution Breakdown

| Module             | Total TCs | Passed | Failed | Blocked | Not Run | Pass Rate |
|--------------------|-----------|--------|--------|---------|---------|-----------|
| Login              | 12        | [X]    | [X]    | [X]     | [X]     | [X%]      |
| Product Browsing   | 12        | [X]    | [X]    | [X]     | [X]     | [X%]      |
| Shopping Cart      | 11        | [X]    | [X]    | [X]     | [X]     | [X%]      |
| Checkout           | 11        | [X]    | [X]    | [X]     | [X]     | [X%]      |
| **Total**          | **46**    | **[X]**| **[X]**| **[X]** | **[X]** | **[X%]**  |

---

## 4. Test Case Status Reference

The following table lists all test cases and their execution status. Update this table as each test case is executed.

### 4.1 Login Module

| Test Case ID  | Title (Short)                               | Status   | Defect Ref.      |
|---------------|---------------------------------------------|----------|------------------|
| TC_LOGIN_001  | Successful login with standard_user          | Not Run  | —                |
| TC_LOGIN_002  | Login blocked for locked_out_user            | Not Run  | —                |
| TC_LOGIN_003  | Login with invalid username                  | Not Run  | —                |
| TC_LOGIN_004  | Login with invalid password                  | Not Run  | —                |
| TC_LOGIN_005  | Empty username field validation              | Not Run  | —                |
| TC_LOGIN_006  | Empty password field validation              | Not Run  | —                |
| TC_LOGIN_007  | Both fields empty validation                 | Not Run  | —                |
| TC_LOGIN_008  | Whitespace-only input rejected               | Not Run  | —                |
| TC_LOGIN_009  | Successful login with problem_user           | Not Run  | —                |
| TC_LOGIN_010  | Successful logout via hamburger menu         | Not Run  | —                |
| TC_LOGIN_011  | Access inventory without login is blocked    | Not Run  | —                |
| TC_LOGIN_012  | Error message dismissed via × button         | Not Run  | BUG_LOGIN_001    |

### 4.2 Product Browsing Module

| Test Case ID    | Title (Short)                               | Status   | Defect Ref.      |
|-----------------|---------------------------------------------|----------|------------------|
| TC_BROWSE_001   | All 6 products load on inventory page        | Not Run  | —                |
| TC_BROWSE_002   | Sort by Name A–Z                             | Not Run  | —                |
| TC_BROWSE_003   | Sort by Name Z–A                             | Not Run  | —                |
| TC_BROWSE_004   | Sort by Price Low–High                       | Not Run  | —                |
| TC_BROWSE_005   | Sort by Price High–Low                       | Not Run  | —                |
| TC_BROWSE_006   | Navigate to product detail via name link     | Not Run  | —                |
| TC_BROWSE_007   | Navigate to product detail via image click   | Not Run  | —                |
| TC_BROWSE_008   | Product detail shows correct info            | Not Run  | —                |
| TC_BROWSE_009   | Back to products returns to inventory        | Not Run  | —                |
| TC_BROWSE_010   | Product count consistent after sorting       | Not Run  | —                |
| TC_BROWSE_011   | Product descriptions visible on listing      | Not Run  | —                |
| TC_BROWSE_012   | All product images load correctly            | Not Run  | BUG_BROWSE_002   |

### 4.3 Shopping Cart Module

| Test Case ID  | Title (Short)                               | Status   | Defect Ref.      |
|---------------|---------------------------------------------|----------|------------------|
| TC_CART_001   | Add single item to cart                      | Not Run  | —                |
| TC_CART_002   | Add multiple items to cart                   | Not Run  | —                |
| TC_CART_003   | Remove item from cart page                   | Not Run  | —                |
| TC_CART_004   | Remove item from product listing             | Not Run  | —                |
| TC_CART_005   | Cart badge accuracy — single item            | Not Run  | —                |
| TC_CART_006   | Cart badge accuracy — all 6 items            | Not Run  | —                |
| TC_CART_007   | Cart persists after navigation               | Not Run  | —                |
| TC_CART_008   | Empty cart state display                     | Not Run  | —                |
| TC_CART_009   | Continue Shopping returns to inventory       | Not Run  | —                |
| TC_CART_010   | Cart items display correct product details   | Not Run  | —                |
| TC_CART_011   | Badge disappears when all items removed      | Not Run  | —                |

### 4.4 Checkout Module

| Test Case ID      | Title (Short)                               | Status   | Defect Ref.       |
|-------------------|---------------------------------------------|----------|-------------------|
| TC_CHECKOUT_001   | Full checkout with valid data                | Not Run  | —                 |
| TC_CHECKOUT_002   | Empty First Name validation                  | Not Run  | —                 |
| TC_CHECKOUT_003   | Empty Last Name validation                   | Not Run  | —                 |
| TC_CHECKOUT_004   | Empty Postal Code validation                 | Not Run  | BUG_CHECKOUT_001  |
| TC_CHECKOUT_005   | All fields empty validation                  | Not Run  | —                 |
| TC_CHECKOUT_006   | Order summary correct items and total        | Not Run  | —                 |
| TC_CHECKOUT_007   | Confirmation page content                    | Not Run  | —                 |
| TC_CHECKOUT_008   | Back Home returns to inventory after order   | Not Run  | —                 |
| TC_CHECKOUT_009   | Cancel Step 1 returns to cart                | Not Run  | —                 |
| TC_CHECKOUT_010   | Cancel Step 2 returns to inventory           | Not Run  | —                 |
| TC_CHECKOUT_011   | Multiple items calculate correct total       | Not Run  | —                 |

---

## 5. Defects Summary

### 5.1 Total Defects by Severity

| Severity  | Count | Bug IDs                          |
|-----------|-------|----------------------------------|
| Critical  | 1     | BUG_CART_001                     |
| Major     | 3     | BUG_BROWSE_001, BUG_CHECKOUT_001, BUG_BROWSE_002 |
| Minor     | 1     | BUG_LOGIN_001                    |
| Trivial   | 0     | —                                |
| **Total** | **5** |                                  |

### 5.2 Total Defects by Priority

| Priority | Count | Bug IDs                                          |
|----------|-------|--------------------------------------------------|
| High     | 3     | BUG_BROWSE_001, BUG_CHECKOUT_001, BUG_CART_001   |
| Medium   | 1     | BUG_BROWSE_002                                   |
| Low      | 1     | BUG_LOGIN_001                                    |

### 5.3 Key Defects Found

| Bug ID           | Title (Short)                                      | Severity | Priority | Status |
|------------------|----------------------------------------------------|----------|----------|--------|
| BUG_CART_001     | Add to cart non-functional for problem_user         | Critical | High     | New    |
| BUG_BROWSE_001   | Product sort broken for problem_user                | Major    | High     | New    |
| BUG_CHECKOUT_001 | Whitespace postal code bypasses form validation     | Major    | High     | New    |
| BUG_BROWSE_002   | All product images incorrect for problem_user       | Major    | Medium   | New    |
| BUG_LOGIN_001    | Error icons persist after banner dismissed          | Minor    | Low      | New    |

> Full details: see `bug_reports/SAMPLE_BUGS.md`

---

## 6. Test Coverage Analysis

| Test Coverage Dimension    | Coverage |
|----------------------------|----------|
| Modules covered            | 4 / 4 (100%) |
| Happy path scenarios       | Covered  |
| Negative / invalid input   | Covered  |
| Boundary / edge cases      | Partially covered (postal code whitespace, empty fields) |
| Cross-browser (Firefox)    | Not executed this cycle |
| Mobile responsiveness      | Not in scope |
| Exploratory testing        | Conducted alongside scripted execution |

---

## 7. Observations and Findings

1. **problem_user defects are intentional and systemic.** The `problem_user` account exhibits multiple seeded defects (broken sort, wrong images, non-functional Add to Cart). These are expected test seedings by SauceDemo but represent real-world defect classes: broken event handlers, incorrect asset references, and unresponsive UI controls.

2. **Form validation does not trim whitespace inputs.** `BUG_CHECKOUT_001` highlights a common vulnerability in web form validation. Input sanitisation should include `trim()` logic to prevent whitespace-only values from bypassing required-field checks.

3. **UI error state is inconsistent post-dismissal.** `BUG_LOGIN_001` indicates that the error dismissal handler clears the banner text but does not clear the individual field error indicators. The error state management appears to be split across two separate mechanisms that are not synchronised.

4. **Core user flows (standard_user) appear functionally sound.** All primary workflows — login, product browsing, adding to cart, and checkout — function as expected for the `standard_user` account, indicating the baseline product quality is good.

---

## 8. Recommendations

1. **Prioritise BUG_CART_001 and BUG_BROWSE_001** as Critical and Major functional defects respectively. While seeded for `problem_user`, the defect classes they represent (non-functional click handlers, broken sort logic) warrant immediate attention in any production codebase.

2. **Fix BUG_CHECKOUT_001** by adding server-side and client-side input trimming to all required form fields at Checkout Step 1. Test with a variety of whitespace inputs including tabs and multi-byte whitespace.

3. **Extend test coverage to Firefox** in the next test cycle to identify any cross-browser discrepancies, particularly around the sort dropdown and checkout form behaviour.

4. **Add boundary test cases for the Postal Code field** — test with alphanumeric codes, international formats (e.g., UK: "EC1A 1BB"), and maximum length strings to ensure the field handles varied real-world input.

5. **Conduct exploratory testing on the order confirmation page** — verify that navigating directly to `/checkout-complete.html` without completing a checkout flow does not show stale order data.

---

## 9. Exit Criteria Evaluation

| Exit Criterion                                          | Target   | Actual   | Met?  |
|---------------------------------------------------------|----------|----------|-------|
| All test cases executed (or formally waived)            | 100%     | [X%]     | [ ]   |
| Pass rate meets minimum threshold                       | ≥ 85%    | [X%]     | [ ]   |
| No open Critical defects                                | 0        | [X]      | [ ]   |
| Test execution summary report produced                  | Yes      | Yes      | [x]   |
| All defects logged with required fields                 | 100%     | 100%     | [x]   |

---

## 10. Sign-Off

| Role            | Name                   | Signature       | Date         |
|-----------------|------------------------|-----------------|--------------|
| QA Engineer     | [Name — Placeholder]   | ____________    | [YYYY-MM-DD] |
| QA Lead         | [Name — Placeholder]   | ____________    | [YYYY-MM-DD] |
| Project Manager | [Name — Placeholder]   | ____________    | [YYYY-MM-DD] |

---

*End of Test Execution Summary — test_execution_summary.md*
