# Login Page Test Automation — Selenium + PyTest

## Summary

This project provides a production-ready, end-to-end UI test suite that validates
the login functionality of [The Internet](https://the-internet.herokuapp.com/login),
a publicly available demo web application.  The suite covers eleven distinct
scenarios — positive login, negative/invalid credentials, empty fields, security
injection payloads, boundary-length inputs, and whitespace-only inputs — and
produces a self-contained HTML report with embedded failure screenshots after
every run.  It is built on the **Page Object Model (POM)** pattern to keep
locators and test logic strictly separated, making the suite easy to extend and
maintain as the UI evolves.

---

## Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11+ | Runtime language |
| Selenium WebDriver | 4.27.1 | Browser automation |
| PyTest | 8.3.4 | Test runner and assertion library |
| pytest-html | 4.1.1 | HTML report generation |
| WebDriver Manager | 4.0.2 | Automatic browser-driver binary download |
| Google Chrome / Mozilla Firefox | Latest stable | Target browsers |

---

## Project Structure

```
login-automation/
├── tests/
│   ├── __init__.py          # Marks the directory as a Python package
│   └── test_login.py        # Parametrized test class — 11 scenarios
├── pages/
│   ├── __init__.py          # Marks the directory as a Python package
│   └── login_page.py        # Page Object Model for the login page
├── utils/
│   ├── __init__.py          # Marks the directory as a Python package
│   └── driver_factory.py    # Creates Chrome / Firefox WebDriver instances
├── data/
│   └── test_data.py         # All credentials, URLs, and scenario definitions
├── reports/
│   ├── .gitkeep             # Keeps the directory in version control
│   ├── report.html          # Auto-generated after each test run
│   └── screenshots/         # Failure screenshots (auto-created on first fail)
├── conftest.py              # Fixtures (driver setup/teardown) + screenshot hook
├── requirements.txt         # Pinned dependency list
├── pytest.ini               # PyTest configuration (paths, addopts, markers)
└── README.md                # This file
```

---

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| **Python 3.11 or higher** | `python --version` to verify |
| **pip** | Bundled with Python 3.4+; upgrade with `pip install --upgrade pip` |
| **Google Chrome** or **Mozilla Firefox** | Latest stable release recommended |
| **Internet access** | WebDriver Manager downloads the matching driver binary on first run |

> **Note:** You do *not* need to install ChromeDriver or GeckoDriver manually.
> WebDriver Manager handles that automatically.

---

## Setup Instructions

### 1. Clone or download the project

```bash
git clone <repository-url>
cd login-automation
```

Or download and extract the ZIP, then `cd login-automation`.

---

### 2. Create and activate a virtual environment

**Windows (Command Prompt / PowerShell)**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure the browser (optional)

The default browser is **Chrome**.  To change it, edit `pytest.ini`:

```ini
[pytest]
browser = firefox    # or chrome
```

You can also override it at runtime without editing the file:

```bash
pytest --browser=firefox
```

Or via environment variable:

```bash
# Windows
set BROWSER=firefox

# macOS / Linux
export BROWSER=firefox
```

**Headless mode** (no visible browser window) is controlled by the `HEADLESS`
environment variable:

```bash
# macOS / Linux
HEADLESS=true pytest

# Windows
set HEADLESS=true && pytest
```

---

### 5. Run all tests

```bash
pytest
```

PyTest will discover every test in the `tests/` directory, execute all 11
parametrized scenarios, and write the HTML report to `reports/report.html`.

---

### 6. Run a specific test by ID

Use the `-k` flag with the test ID (the `test_id` field from `test_data.py`):

```bash
pytest -k TC001_valid_credentials
pytest -k TC007_sql_injection
pytest -k TC009_boundary_username_255_chars
```

Or use the full nodeid syntax:

```bash
pytest "tests/test_login.py::TestLogin::test_login_scenario[TC003_invalid_password]"
```

Run all security-tagged scenarios only:

```bash
pytest -m security
```

---

### 7. View the HTML report

After a run, open the self-contained report in any browser:

**Windows**
```bash
start reports\report.html
```

**macOS**
```bash
open reports/report.html
```

**Linux**
```bash
xdg-open reports/report.html
```

The report includes per-test status, duration, captured log output, and —
for any failed test — an embedded screenshot taken at the moment of failure.

---

## Test Scenarios

| Test ID | Input Type | Username | Password | Expected Outcome |
|---------|-----------|----------|----------|-----------------|
| TC001_valid_credentials | Valid credentials | `tomsmith` | `SuperSecretPassword!` | Redirect to `/secure` |
| TC002_invalid_username | Invalid username | `wronguser` | `SuperSecretPassword!` | Error: "Your username is invalid!" |
| TC003_invalid_password | Invalid password | `tomsmith` | `wrongpassword` | Error: "Your password is invalid!" |
| TC004_empty_username | Empty username | *(empty)* | `SuperSecretPassword!` | Error: "Your username is invalid!" |
| TC005_empty_password | Empty password | `tomsmith` | *(empty)* | Error: "Your password is invalid!" |
| TC006_both_fields_empty | Both fields empty | *(empty)* | *(empty)* | Error: "Your username is invalid!" |
| TC007_sql_injection | SQL injection payload | `' OR '1'='1' --` | `' OR '1'='1' --` | Error: "Your username is invalid!" |
| TC008_xss_injection | XSS payload | `<script>alert('XSS')</script>` | *(same)* | Error: "Your username is invalid!" |
| TC009_boundary_username_255_chars | 255-char username | 255 × `a` | `SuperSecretPassword!` | Error: "Your username is invalid!" |
| TC010_boundary_password_255_chars | 255-char password | `tomsmith` | 255 × `a` | Error: "Your password is invalid!" |
| TC011_whitespace_only_inputs | Whitespace-only inputs | `"   "` | `"   "` | Error: "Your username is invalid!" |

---

## Markers Reference

| Marker | Applied to |
|--------|-----------|
| `login` | All tests in the suite |
| `positive` | TC001 (successful login) |
| `negative` | All failure-path tests |
| `security` | TC007, TC008 (injection tests) |
| `boundary` | TC009, TC010 (255-char inputs) |

Run tests by marker: `pytest -m "security or boundary"`

---

## Known Limitations and Assumptions

1. **Demo site availability** — Tests rely on the publicly hosted site
   `https://the-internet.herokuapp.com/login`.  If the site is down or rate-
   limiting requests, tests will fail with connection/timeout errors rather than
   assertion errors.

2. **Error message wording** — Assertions match substrings of the flash message
   text.  If the demo site changes its error copy, the expected strings in
   `data/test_data.py` must be updated accordingly.

3. **TC006 (both empty)** — The application validates the username field first,
   so an empty-username error is expected even though the password is also empty.

4. **TC009 / TC010 (boundary inputs)** — The 255-character strings are simply
   rejected as invalid credentials; the tests do *not* assert that the field
   enforces a character limit at the UI level.

5. **TC007 / TC008 (injection)** — These tests verify that the application
   refuses the malicious inputs.  They are functional / black-box tests only and
   do not inspect server-side sanitisation logic.

6. **Browser versions** — WebDriver Manager downloads the driver that matches
   the browser installed on the machine.  Always keep your browser up to date
   to avoid driver-version mismatches.

7. **Parallel execution** — The suite is designed for sequential execution.
   Running tests in parallel (e.g. with `pytest-xdist`) is not configured and
   has not been tested.

---

## Author

| Field | Value |
|-------|-------|
| Name | *(replace with your name)* |
| Email | *(replace with your email)* |
| Project | Login Page Test Automation — Selenium + PyTest |
| Date | March 2026 |
