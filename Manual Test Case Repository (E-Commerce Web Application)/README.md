# Manual Test Case Repository — E-Commerce Web Application

**Application Under Test:** [SauceDemo](https://www.saucedemo.com)
**Testing Type:** Manual Functional Testing
**Author:** [Your Name]
**Status:** Ready for Execution

---

## Project Summary

This repository is a professional manual testing portfolio artifact demonstrating structured QA practices aligned with the **Software Testing Life Cycle (STLC)**. It was built to test **SauceDemo** — a publicly available e-commerce demo application by Sauce Labs that simulates a real-world online storefront.

The repository covers four core e-commerce modules: **Login**, **Product Browsing**, **Shopping Cart**, and **Checkout**. It includes a formal test plan, 46 structured test cases, a reusable bug report template, 5 sample bug reports, a requirements traceability matrix (RTM), and a test execution summary report.

**What this repository demonstrates:**
- Structured test case design using equivalence partitioning and boundary value analysis
- Professional bug reporting with severity/priority classification
- Requirements traceability from user stories to test cases
- STLC-aligned documentation across all testing phases
- Black-box, functional, and negative testing techniques

---

## Scope

| Module             | Test Cases | Testing Type                              |
|--------------------|------------|-------------------------------------------|
| Login              | 12         | Functional, Negative, Boundary, Security-adjacent |
| Product Browsing   | 12         | Functional, UI Validation                 |
| Shopping Cart      | 11         | Functional, State Persistence             |
| Checkout           | 11         | Functional, Validation, Boundary          |
| **Total**          | **46**     |                                           |

---

## Repository Structure

```
manual-ecommerce-testing/
├── test_plan/
│   └── test_plan.md                    ← Master test plan document
├── test_cases/
│   ├── TC_LOGIN.md                     ← 12 login test cases
│   ├── TC_PRODUCT_BROWSING.md          ← 12 product browsing test cases
│   ├── TC_CART.md                      ← 11 shopping cart test cases
│   └── TC_CHECKOUT.md                  ← 11 checkout test cases
├── bug_reports/
│   ├── BUG_TEMPLATE.md                 ← Reusable bug report template
│   └── SAMPLE_BUGS.md                  ← 5 fully documented sample bug reports
├── test_summary/
│   └── test_execution_summary.md       ← Post-execution metrics and sign-off
├── traceability/
│   └── rtm.md                          ← Requirements Traceability Matrix
└── README.md                           ← This file
```

---

## How to Navigate This Repository

**If you are reading this for the first time**, follow this order:

1. **`test_plan/test_plan.md`** — Start here. Understand scope, approach, entry/exit criteria, risks, and environment.
2. **`traceability/rtm.md`** — Review the requirements (user stories) that drive the test cases.
3. **`test_cases/TC_LOGIN.md`** → `TC_PRODUCT_BROWSING.md` → `TC_CART.md` → `TC_CHECKOUT.md` — Read the test cases module by module.
4. **`bug_reports/BUG_TEMPLATE.md`** — Understand the defect reporting standard before execution.
5. **`bug_reports/SAMPLE_BUGS.md`** — Review sample defects to understand the expected quality of bug reports.
6. **`test_summary/test_execution_summary.md`** — Review this template; update it after test execution with real results.

**If you are executing tests**, follow this order:

1. Validate the test environment (URL accessible, correct browser and OS).
2. Execute test cases module by module, starting with Login.
3. Update the `Actual Result` and `Status` fields in each test case file.
4. Log any defects using the template in `bug_reports/BUG_TEMPLATE.md`.
5. Update the traceability matrix if new test cases are added.
6. Complete the `test_summary/test_execution_summary.md` at cycle close.

---

## How to Adapt This Repository for a New Application

1. **Update the test plan** (`test_plan/test_plan.md`): Change the AUT name, URL, scope, environment, and risk register.
2. **Replace test cases**: Update the TC files with steps and data specific to the new application. Keep the same table structure and ID conventions.
3. **Rewrite user stories in the RTM** (`traceability/rtm.md`): Replace SauceDemo-specific stories with requirements for the new application.
4. **Add new module test case files** as needed (e.g., `TC_SEARCH.md`, `TC_USER_PROFILE.md`) following the existing naming and formatting conventions.
5. **Clear sample bugs** from `SAMPLE_BUGS.md` and replace with real defects found during execution.
6. **Update the execution summary** template with the new module names and test case counts.

---

## Test Environment

| Parameter            | Value |
|----------------------|-------|
| **Application URL**  | https://www.saucedemo.com |
| **Primary Browser**  | Google Chrome (latest stable) |
| **Secondary Browser**| Mozilla Firefox (latest stable) |
| **Operating System** | Windows 11 / macOS Ventura or later |
| **Screen Resolution**| 1920×1080 (primary) |
| **Network**          | Standard broadband |
| **Test Type**        | Manual — no automation framework |

---

## Test Credentials

The following credentials are publicly documented by SauceDemo for testing purposes:

| Username                   | Password       | Expected Behaviour |
|----------------------------|----------------|--------------------|
| `standard_user`            | `secret_sauce` | Full access — primary test user |
| `locked_out_user`          | `secret_sauce` | Login blocked with error message |
| `problem_user`             | `secret_sauce` | Login succeeds; known UI/functional defects present |
| `performance_glitch_user`  | `secret_sauce` | Login succeeds; artificially slow response |
| `error_user`               | `secret_sauce` | Login succeeds; cart and checkout errors present |
| `visual_user`              | `secret_sauce` | Login succeeds; visual layout defects present |

> **Note:** These credentials are publicly provided at https://www.saucedemo.com for demo and testing purposes only. Do not use them in any production or sensitive context.

---

## STLC Phase Mapping

| STLC Phase              | Document(s)                                                            |
|-------------------------|------------------------------------------------------------------------|
| Requirement Analysis    | `traceability/rtm.md` (user stories section)                           |
| Test Planning           | `test_plan/test_plan.md`                                               |
| Test Case Design        | `test_cases/TC_LOGIN.md`, `TC_PRODUCT_BROWSING.md`, `TC_CART.md`, `TC_CHECKOUT.md` |
| Test Environment Setup  | `test_plan/test_plan.md` (Section 7 — Test Environment)                |
| Test Execution          | Test case files (Actual Result + Status fields), `bug_reports/SAMPLE_BUGS.md` |
| Test Closure            | `test_summary/test_execution_summary.md`, `traceability/rtm.md`        |

---

## Naming Conventions

| Artifact          | Convention                        | Example            |
|-------------------|-----------------------------------|--------------------|
| Test Case IDs     | `TC_[MODULE]_[3-digit number]`    | `TC_LOGIN_001`     |
| Bug IDs           | `BUG_[MODULE]_[3-digit number]`   | `BUG_CART_003`     |
| Requirement IDs   | `REQ-[MODULE]-[2-digit number]`   | `REQ-CHECKOUT-02`  |
| Module codes      | `LOGIN`, `BROWSE`, `CART`, `CHECKOUT` | —               |

---

## How to Extend This Repository

**Adding a new module:**
1. Create a new file: `test_cases/TC_[MODULENAME].md`
2. Add the new module's user stories to `traceability/rtm.md`
3. Link the new test cases in the RTM reverse traceability table
4. Update the scope table in this README
5. Add the module row to the execution summary breakdown table

**Adding new test cases to an existing module:**
1. Add new rows to the appropriate `test_cases/TC_[MODULE].md` file
2. Follow the ID sequence (e.g., if the last case is `TC_LOGIN_012`, the next is `TC_LOGIN_013`)
3. Link the new test case to a requirement in `traceability/rtm.md`
4. Update the test case count in the README scope table and the execution summary

**Logging a new defect:**
1. Copy the template from `bug_reports/BUG_TEMPLATE.md`
2. Assign the next sequential Bug ID for the relevant module
3. Fill all required fields
4. Add a row to the defects summary table in `test_summary/test_execution_summary.md`

---

## Author

| Field        | Value |
|--------------|-------|
| **Name**     | [Your Full Name] |
| **Role**     | QA Engineer |
| **Contact**  | [your.email@example.com] |
| **LinkedIn** | [linkedin.com/in/yourprofile] |
| **GitHub**   | [github.com/yourusername] |

---

*This repository was prepared as a QA portfolio artifact. All test cases, bug reports, and documentation follow industry-standard manual testing practices aligned with the ISTQB Foundation Level syllabus and STLC framework.*
