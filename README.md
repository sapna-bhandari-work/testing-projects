# QA Engineering Portfolio — Sapna Bhandari

> A consolidated repository of three end-to-end quality assurance projects demonstrating manual testing, test automation, and API validation skills across real-world web applications.

---

## Portfolio Overview

| # | Project | Type | Target Application | Primary Tools |
|---|---------|------|--------------------|---------------|
| 1 | Login Page Test Automation | Automated | the-internet.herokuapp.com | Selenium WebDriver, PyTest, Python |
| 2 | REST API Testing Suite | Automated + Manual | JSONPlaceholder API | Postman, Python Requests, PyTest |
| 3 | Manual Test Case Repository | Manual | saucedemo.com | Markdown, STLC Documentation |

---

## Project 1 — Login Page Test Automation (Selenium + PyTest)

### Summary

An automated regression testing suite for web-based login functionality, built using the Page Object Model (POM) design pattern. The suite covers 10+ login scenarios including valid credentials, invalid inputs, boundary values, and injection attempts, executed against a live demo application. Tests generate HTML reports on every run and capture screenshots automatically on failure.

### Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Selenium WebDriver | Browser automation |
| PyTest | Test framework and runner |
| WebDriver Manager | Automatic browser driver management |
| pytest-html | HTML report generation |

### Project Structure

```
login-automation/
├── tests/
│   └── test_login.py          # Parameterized test scenarios
├── pages/
│   └── login_page.py          # Page Object Model — locators and actions
├── utils/
│   └── driver_factory.py      # WebDriver initialisation, browser config
├── data/
│   └── test_data.py           # All test inputs and expected outcomes
├── reports/                   # Auto-generated HTML reports
├── conftest.py                # Fixtures, WebDriver teardown, screenshot hook
├── requirements.txt           # Pinned dependencies
└── pytest.ini                 # Test configuration, report path, markers
```

### Setup and Execution

**Prerequisites:** Python 3.8+, Google Chrome or Firefox, pip

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all tests
pytest

# 4. Run a specific test by ID
pytest -k "test_invalid_password"

# 5. View the HTML report
open reports/report.html
```

### Test Scenario Coverage

| Test ID | Input Type | Expected Outcome |
|---------|-----------|-----------------|
| TC_LOGIN_001 | Valid credentials | Redirect to /secure |
| TC_LOGIN_002 | Invalid username | Error message displayed |
| TC_LOGIN_003 | Invalid password | Error message displayed |
| TC_LOGIN_004 | Empty username | Validation error |
| TC_LOGIN_005 | Empty password | Validation error |
| TC_LOGIN_006 | Both fields empty | Validation error |
| TC_LOGIN_007 | SQL injection input | No crash, error handled |
| TC_LOGIN_008 | XSS injection input | No crash, input sanitised |
| TC_LOGIN_009 | 255-character username | Boundary handled |
| TC_LOGIN_010 | 255-character password | Boundary handled |
| TC_LOGIN_011 | Whitespace-only inputs | Validation error |

---

## Project 2 — REST API Testing Suite (Postman + Python Requests)

### Summary

A dual-implementation API testing suite that validates the JSONPlaceholder REST API across GET, POST, PUT, and DELETE operations. The project is built twice in parallel — once as an importable Postman collection for exploratory and manual validation, and once as a Python-based automated suite integrated with PyTest and JSON schema validation. Covers 15+ scenarios including status codes, response schema correctness, field-level assertions, and response time thresholds.

### Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core automation language |
| Requests | HTTP client for API calls |
| PyTest | Test framework |
| jsonschema | JSON Schema Draft-07 response validation |
| Postman | Manual + scripted API testing |
| Newman CLI | Postman collection CI execution |
| pytest-html | Automated report generation |

### Project Structure

```
api-testing-suite/
├── postman/
│   ├── JSONPlaceholder_Collection.json    # Importable Postman collection (v2.1)
│   └── JSONPlaceholder_Environment.json  # Environment variables (base_url, IDs)
├── python_suite/
│   ├── tests/
│   │   ├── test_get.py                   # GET request scenarios
│   │   ├── test_post.py                  # POST request scenarios
│   │   ├── test_put.py                   # PUT request scenarios
│   │   └── test_delete.py               # DELETE request scenarios
│   ├── utils/
│   │   ├── api_client.py                 # Reusable ApiClient wrapper class
│   │   └── schema_validator.py           # JSON schema validation utility
│   ├── schemas/
│   │   ├── post_schema.json              # Schema for /posts responses
│   │   └── user_schema.json             # Schema for /users responses
│   ├── data/
│   │   └── payloads.py                  # All request body definitions
│   ├── conftest.py                       # Session-scoped ApiClient fixture
│   ├── requirements.txt
│   └── pytest.ini
└── README.md
```

### Setup and Execution

**Option A — Python Suite**

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all API tests
pytest python_suite/

# 4. View the HTML report
open python_suite/reports/report.html
```

**Option B — Postman Collection**

```bash
# Import into Postman Desktop:
# File > Import > select JSONPlaceholder_Collection.json
# Then import JSONPlaceholder_Environment.json and set as active environment

# Or run via Newman CLI (for CI pipelines):
npm install -g newman
newman run postman/JSONPlaceholder_Collection.json \
  -e postman/JSONPlaceholder_Environment.json
```

### Test Coverage Matrix

| Endpoint | Method | Scenario | Expected Status |
|----------|--------|----------|----------------|
| /posts | GET | Returns non-empty list | 200 |
| /posts/1 | GET | Schema validation | 200 |
| /posts/9999 | GET | Non-existent resource | 404 |
| /users/1 | GET | Schema validation | 200 |
| /posts?userId=1 | GET | Filter by userId | 200 |
| /posts | POST | Valid payload, id returned | 201 |
| /posts | POST | Empty body edge case | 201 |
| /posts/1 | PUT | Updated title reflected | 200 |
| /posts/1 | DELETE | Empty object returned | 200 |
| Multiple | ALL | Response time under 2000ms | — |

> **Note:** JSONPlaceholder is a mock API. Data mutations (POST, PUT, DELETE) are simulated and not persisted between requests.

---

## Project 3 — Manual Test Case Repository (E-Commerce Web Application)

### Summary

A complete manual QA documentation repository for an e-commerce web application, structured around the Software Testing Life Cycle (STLC). Covers four core user journeys — login, product browsing, cart management, and checkout — with 40+ structured test cases, a formal test plan, sample bug reports, a test execution summary, and a Requirements Traceability Matrix (RTM). Designed as a reference-grade QA artifact suitable for professional use or portfolio demonstration.

### Target Application

**URL:** https://www.saucedemo.com

**Test Credentials:**

| Username | Password | Account Type |
|----------|----------|-------------|
| standard_user | secret_sauce | Standard access |
| locked_out_user | secret_sauce | Locked account (negative test) |
| problem_user | secret_sauce | UI bug simulation |

### Project Structure

```
manual-ecommerce-testing/
├── test_plan/
│   └── test_plan.md                      # Scope, approach, entry/exit criteria
├── test_cases/
│   ├── TC_LOGIN.md                       # 10+ login test cases
│   ├── TC_PRODUCT_BROWSING.md            # 10+ browsing and sort test cases
│   ├── TC_CART.md                        # 10+ cart management test cases
│   └── TC_CHECKOUT.md                    # 10+ checkout flow test cases
├── bug_reports/
│   ├── BUG_TEMPLATE.md                   # Reusable bug report format
│   └── SAMPLE_BUGS.md                    # 5 realistic sample bug reports
├── test_summary/
│   └── test_execution_summary.md         # Metrics, module breakdown, sign-off
├── traceability/
│   └── rtm.md                            # Requirements Traceability Matrix
└── README.md
```

### STLC Phase Mapping

| STLC Phase | Document |
|------------|---------|
| Requirement Analysis | `traceability/rtm.md` |
| Test Planning | `test_plan/test_plan.md` |
| Test Case Development | `test_cases/*.md` |
| Test Execution | `test_summary/test_execution_summary.md` |
| Defect Reporting | `bug_reports/SAMPLE_BUGS.md` |
| Test Closure | `test_summary/test_execution_summary.md` |

### Test Case Coverage Summary

| Module | Test Cases | Testing Type |
|--------|-----------|-------------|
| Login | 10 | Functional, Negative, Boundary |
| Product Browsing | 10 | Functional, UI Validation |
| Cart Management | 10 | Functional, State Persistence |
| Checkout | 10 | End-to-End, Negative |
| **Total** | **40+** | — |

### Test Case Structure

Every test case follows this standardised format:

| Field | Description |
|-------|-------------|
| Test Case ID | `TC_[MODULE]_[001]` |
| Title | Short descriptive title |
| Module | Feature area |
| Priority | High / Medium / Low |
| Preconditions | Required state before execution |
| Test Steps | Numbered, step-by-step actions |
| Test Data | Exact inputs used |
| Expected Result | Observable correct behaviour |
| Actual Result | Filled during execution |
| Status | Pass / Fail / Blocked / Not Run |
| Severity | Critical / Major / Minor / Trivial |

### Bug ID Convention

All defects follow the format: `BUG_[MODULE]_[001]`

> **Severity vs Priority:** Severity refers to the impact of a defect on the system's functionality. Priority refers to the urgency with which the defect should be fixed. These are tracked independently throughout this repository.

---

## Repository Navigation Guide

If you are reviewing this portfolio for the first time, the recommended reading order is as follows.

Start with this README to understand the scope of all three projects. For Project 1, begin with `conftest.py` to understand the test setup, then `data/test_data.py` to see test inputs, then `tests/test_login.py` for the actual test logic. For Project 2, start with `utils/api_client.py` to understand the client wrapper, then review any one test file alongside the corresponding schema in `/schemas/`. For Project 3, begin with `test_plan/test_plan.md`, then `traceability/rtm.md`, then any module's test cases.

---

## Author

**Sapna Bhandari**
B.Sc. Computer Science — Indira College of Commerce & Science, Pune (2026)
[LinkedIn](https://www.linkedin.com/in/bhandarisapna) | [GitHub](https://github.com/sapna-bhandari-work/testing-projects) | sapna.bhandari.work@gmail.com
