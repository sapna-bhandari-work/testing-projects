# Test Plan — E-Commerce Web Application (SauceDemo)

**Document Version:** 1.0
**Prepared By:** [QA Engineer Name]
**Review Date:** [Date]
**Approval Date:** [Date]
**Status:** Draft

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Scope and Objectives](#2-scope-and-objectives)
3. [Features to Be Tested](#3-features-to-be-tested)
4. [Features Out of Scope](#4-features-out-of-scope)
5. [Test Approach](#5-test-approach)
6. [Entry and Exit Criteria](#6-entry-and-exit-criteria)
7. [Test Environment](#7-test-environment)
8. [Test Data](#8-test-data)
9. [Roles and Responsibilities](#9-roles-and-responsibilities)
10. [Risks and Mitigations](#10-risks-and-mitigations)
11. [Test Deliverables](#11-test-deliverables)
12. [Test Schedule](#12-test-schedule)

---

## 1. Introduction

This document defines the test plan for manual functional testing of the SauceDemo e-commerce web application, accessible at **https://www.saucedemo.com**. SauceDemo is a publicly available demo application built by Sauce Labs and serves as a representative e-commerce storefront for QA practice and portfolio demonstration.

This test plan governs the planning, execution, and reporting of all manual test activities covered in this repository. It is aligned with the **Software Testing Life Cycle (STLC)** and follows structured, professional QA practices.

---

## 2. Scope and Objectives

### 2.1 Objectives

- Validate the functional correctness of core e-commerce user flows on SauceDemo.
- Identify and document defects across the Login, Product Browsing, Shopping Cart, and Checkout modules.
- Produce a reusable, professional-grade QA artifact suitable for a portfolio.
- Demonstrate structured test case design, bug reporting, and traceability practices.

### 2.2 In-Scope Modules

| Module             | Description                                            |
|--------------------|--------------------------------------------------------|
| Login              | Authentication flows — valid, invalid, locked users    |
| Product Browsing   | Product listing, sorting, and product detail pages     |
| Shopping Cart      | Add, remove, and view items in the cart                |
| Checkout           | Order information input, order summary, confirmation   |

### 2.3 Testing Types In Scope

- **Functional Testing** — Verification that features work as specified.
- **Negative Testing** — Validation of error handling with invalid inputs.
- **Boundary Value Testing** — Edge case inputs in form fields.
- **UI Validation** — Verification of labels, messages, and page elements.
- **Regression Testing** (scenario-based) — Ensure core flows are unbroken.

---

## 3. Features to Be Tested

### 3.1 Login Module
- Login with valid credentials (standard_user)
- Login with locked-out user (locked_out_user)
- Login with invalid username / password combinations
- Login with empty username and/or password fields
- Error message display and accuracy
- Logout functionality

### 3.2 Product Browsing Module
- Product listing page load and item count
- Product sort by: Name (A–Z), Name (Z–A), Price (Low–High), Price (High–Low)
- Navigation to individual product detail pages
- Product image, name, description, and price display
- Navigation back to the product listing from a detail page

### 3.3 Shopping Cart Module
- Adding a single product to the cart
- Adding multiple products to the cart
- Removing a product from the cart (via cart page and product listing)
- Cart badge count accuracy
- Cart state persistence after navigating away and returning
- Empty cart state display

### 3.4 Checkout Module
- Initiating checkout from cart page
- Entering valid customer information (first name, last name, postal code)
- Form validation on empty required fields
- Checkout step 1 → step 2 navigation (order summary)
- Price, tax, and total calculation on order summary page
- Order confirmation page display and content
- "Finish" button completing the order
- "Continue Shopping" post-checkout navigation
- Cancelling checkout

---

## 4. Features Out of Scope

The following features are explicitly excluded from this test cycle:

| Feature                        | Reason for Exclusion                              |
|-------------------------------|---------------------------------------------------|
| Payment gateway integration    | SauceDemo does not implement real payment flows   |
| User registration / sign-up    | Not available on the application                  |
| Account profile management     | Not available on the application                  |
| Wish list / favorites          | Not available on the application                  |
| Product search / search bar    | Not available on the application                  |
| Order history / tracking       | Not available on the application                  |
| REST API / backend testing     | Out of scope; this is a UI-only test plan         |
| Cross-browser compatibility    | Documented but not fully matrix-tested            |
| Performance / load testing     | Outside the scope of functional manual testing    |
| Security / penetration testing | Beyond scope of this QA portfolio artifact        |
| Accessibility testing          | Not covered in this version of the test plan      |
| Mobile responsiveness          | Not covered in this version of the test plan      |

---

## 5. Test Approach

### 5.1 Testing Technique
- **Black-Box Testing** — All tests are based on observable inputs and outputs without knowledge of the internal source code.
- **Equivalence Partitioning** — Valid and invalid input classes are used to design login and checkout test cases.
- **Boundary Value Analysis** — Applied to form fields with character or data constraints.
- **Exploratory Testing** — Ad-hoc exploration of module behaviour following scripted execution.

### 5.2 Test Execution Approach
1. Test cases will be executed manually by a QA engineer.
2. Each test case will be executed in a fresh browser session unless stated otherwise.
3. Defects identified during execution will be logged immediately in the bug report format defined in `bug_reports/BUG_TEMPLATE.md`.
4. Test results (Actual Result, Status) will be updated in the test case files post-execution.
5. A test execution summary will be produced at the close of each test cycle.

### 5.3 Defect Management
- All defects will be logged using the standard template defined in `bug_reports/BUG_TEMPLATE.md`.
- Defects will be classified by **Severity** (impact on the system) and **Priority** (urgency of fix).
- Defect lifecycle: New → Open → In Progress → Fixed → Retest → Closed / Rejected.

---

## 6. Entry and Exit Criteria

### 6.1 Entry Criteria

| Criterion                                               | Owner         |
|--------------------------------------------------------|---------------|
| Test plan has been reviewed and approved                | QA Lead       |
| Test cases have been authored and peer-reviewed         | QA Engineer   |
| The application under test (AUT) is accessible at URL  | QA Engineer   |
| Test environment details are confirmed                  | QA Engineer   |
| Test data (credentials, product info) is available      | QA Engineer   |

### 6.2 Exit Criteria

| Criterion                                               | Threshold     |
|--------------------------------------------------------|---------------|
| All test cases have been executed (or waived)          | 100% executed |
| Pass rate meets minimum threshold                      | ≥ 85% pass    |
| No open Critical- or High-severity defects             | 0 open        |
| Test execution summary report has been produced         | Completed     |
| All defects have been logged with required fields       | 100% logged   |

### 6.3 Suspension Criteria
Test execution will be suspended if:
- The application is completely inaccessible (HTTP 5xx or DNS failure).
- More than 30% of test cases are blocked due to a single blocker defect.
- A Critical defect prevents execution of an entire module.

---

## 7. Test Environment

### 7.1 Application Under Test

| Parameter       | Value                          |
|-----------------|-------------------------------|
| Application     | SauceDemo E-Commerce Demo      |
| URL             | https://www.saucedemo.com      |
| Application Type | Web (Single Page Application) |
| Technology Stack | React.js (front-end)          |

### 7.2 Test Environment Specifications

| Parameter         | Value                                          |
|-------------------|------------------------------------------------|
| Operating System  | Windows 11 / macOS Ventura (or later)          |
| Primary Browser   | Google Chrome (latest stable release)          |
| Secondary Browser | Mozilla Firefox (latest stable release)        |
| Screen Resolution | 1920×1080 (primary), 1366×768 (secondary)      |
| Network           | Standard broadband internet connection         |
| Test Execution    | Manual — no automation framework               |

### 7.3 Browser Compatibility Notes
- Primary execution is performed on **Google Chrome (latest)**.
- Results may be spot-checked on **Mozilla Firefox** for critical paths.
- Internet Explorer and legacy Edge are not in scope.

---

## 8. Test Data

### 8.1 Login Credentials

| Username                  | Password      | Expected Behaviour                        |
|--------------------------|---------------|-------------------------------------------|
| standard_user             | secret_sauce  | Successful login — redirects to inventory |
| locked_out_user           | secret_sauce  | Login blocked — error message displayed   |
| problem_user              | secret_sauce  | Login succeeds — known UI defects present |
| performance_glitch_user   | secret_sauce  | Login succeeds — delayed response         |
| error_user                | secret_sauce  | Login succeeds — cart/checkout errors     |
| visual_user               | secret_sauce  | Login succeeds — visual layout defects    |
| invalid_user              | secret_sauce  | Login fails — error message               |
| standard_user             | wrong_pass    | Login fails — error message               |

### 8.2 Checkout Test Data

| Field       | Valid Data          | Invalid Data |
|-------------|---------------------|--------------|
| First Name  | Test                | (empty)      |
| Last Name   | User                | (empty)      |
| Postal Code | 12345               | (empty)      |

---

## 9. Roles and Responsibilities

| Role             | Name                  | Responsibility                                           |
|------------------|-----------------------|----------------------------------------------------------|
| QA Engineer      | [Name — Placeholder]  | Test case authoring, test execution, defect logging      |
| QA Lead          | [Name — Placeholder]  | Test plan review, defect triage, exit criteria sign-off  |
| Project Manager  | [Name — Placeholder]  | Schedule coordination, risk escalation                   |
| Developer        | [Name — Placeholder]  | Defect investigation and resolution                      |

---

## 10. Risks and Mitigations

| Risk ID | Risk Description                                           | Likelihood | Impact   | Mitigation Strategy                                                     |
|---------|------------------------------------------------------------|------------|----------|-------------------------------------------------------------------------|
| R-01    | Demo site may be temporarily unavailable                   | Low        | High     | Validate site availability before each test session; reschedule if down |
| R-02    | Application behaviour may change without notice            | Medium     | High     | Baseline screenshots at test start; note app version/date               |
| R-03    | Known defects in problem_user affect test results          | High       | Medium   | Document expected known defects; use standard_user as primary user      |
| R-04    | Inconsistency across browsers for UI tests                 | Medium     | Low      | Focus primary execution on Chrome; note browser for each session        |
| R-05    | Single QA resource — no peer review of test cases          | Medium     | Medium   | Use self-review checklist; follow naming and format standards strictly   |
| R-06    | Scope creep — expanding beyond defined modules             | Low        | Medium   | Freeze scope at plan approval; log out-of-scope findings as observations |

---

## 11. Test Deliverables

| Deliverable                    | File Path                                      | STLC Phase         |
|-------------------------------|------------------------------------------------|--------------------|
| Test Plan                      | `test_plan/test_plan.md`                      | Test Planning      |
| Login Test Cases               | `test_cases/TC_LOGIN.md`                      | Test Case Design   |
| Product Browsing Test Cases    | `test_cases/TC_PRODUCT_BROWSING.md`           | Test Case Design   |
| Cart Test Cases                | `test_cases/TC_CART.md`                       | Test Case Design   |
| Checkout Test Cases            | `test_cases/TC_CHECKOUT.md`                   | Test Case Design   |
| Bug Report Template            | `bug_reports/BUG_TEMPLATE.md`                 | Test Execution     |
| Sample Bug Reports             | `bug_reports/SAMPLE_BUGS.md`                  | Test Execution     |
| Test Execution Summary         | `test_summary/test_execution_summary.md`      | Test Closure       |
| Requirements Traceability Matrix | `traceability/rtm.md`                       | Test Planning / Closure |

---

## 12. Test Schedule

| Activity                          | Planned Start    | Planned End      | Owner        |
|----------------------------------|------------------|------------------|--------------|
| Test plan authoring               | [Start Date]     | [End Date]       | QA Engineer  |
| Test case design                  | [Start Date]     | [End Date]       | QA Engineer  |
| Test plan review and approval     | [Start Date]     | [End Date]       | QA Lead      |
| Test environment validation       | [Start Date]     | [End Date]       | QA Engineer  |
| Test execution — Cycle 1          | [Start Date]     | [End Date]       | QA Engineer  |
| Defect logging and triage         | [Start Date]     | [End Date]       | QA Engineer  |
| Defect retest (if applicable)     | [Start Date]     | [End Date]       | QA Engineer  |
| Test summary report               | [Start Date]     | [End Date]       | QA Engineer  |
| Test closure and sign-off         | [Start Date]     | [End Date]       | QA Lead      |

---

*End of Test Plan*
