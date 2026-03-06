"""
Test data module defining all login scenarios for parametrized test execution.

All credentials and expected outcomes are centralised here so that
no sensitive values are hard-coded in the test files themselves.
"""

# ---------------------------------------------------------------------------
# Site constants
# ---------------------------------------------------------------------------
BASE_URL: str = "https://the-internet.herokuapp.com/login"
SECURE_URL_FRAGMENT: str = "/secure"

# Valid credentials for the-internet.herokuapp.com
VALID_USERNAME: str = "tomsmith"
VALID_PASSWORD: str = "SuperSecretPassword!"

# ---------------------------------------------------------------------------
# Error messages expected from the application
# ---------------------------------------------------------------------------
ERROR_INVALID_USERNAME: str = "Your username is invalid!"
ERROR_INVALID_PASSWORD: str = "Your password is invalid!"

# ---------------------------------------------------------------------------
# Boundary helpers
# ---------------------------------------------------------------------------
BOUNDARY_STRING_255: str = "a" * 255

# ---------------------------------------------------------------------------
# Test scenarios
# ---------------------------------------------------------------------------
# Each scenario is a dict with the following keys:
#   test_id              – unique identifier used as the pytest parametrize ID
#   username             – value to type into the username field
#   password             – value to type into the password field
#   expect_success       – True  → assert redirect to SECURE_URL_FRAGMENT
#                          False → assert error message is shown
#   expected_url_fragment– URL substring expected after a SUCCESSFUL login
#   expected_error       – substring of the error flash message (failure cases)
#   description          – human-readable summary of the scenario
#   marks                – list of custom pytest mark names to apply
TEST_SCENARIOS: list[dict] = [
    # ------------------------------------------------------------------
    # TC001 – Positive: valid credentials
    # ------------------------------------------------------------------
    {
        "test_id": "TC001_valid_credentials",
        "username": VALID_USERNAME,
        "password": VALID_PASSWORD,
        "expect_success": True,
        "expected_url_fragment": SECURE_URL_FRAGMENT,
        "expected_error": None,
        "description": "Valid credentials — should redirect to the secure area.",
        "marks": ["positive", "login"],
    },
    # ------------------------------------------------------------------
    # TC002 – Negative: invalid username
    # ------------------------------------------------------------------
    {
        "test_id": "TC002_invalid_username",
        "username": "wronguser",
        "password": VALID_PASSWORD,
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "Invalid username — should display username error.",
        "marks": ["negative", "login"],
    },
    # ------------------------------------------------------------------
    # TC003 – Negative: invalid password
    # ------------------------------------------------------------------
    {
        "test_id": "TC003_invalid_password",
        "username": VALID_USERNAME,
        "password": "wrongpassword",
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_PASSWORD,
        "description": "Invalid password — should display password error.",
        "marks": ["negative", "login"],
    },
    # ------------------------------------------------------------------
    # TC004 – Negative: empty username
    # ------------------------------------------------------------------
    {
        "test_id": "TC004_empty_username",
        "username": "",
        "password": VALID_PASSWORD,
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "Empty username — should display username error.",
        "marks": ["negative", "login"],
    },
    # ------------------------------------------------------------------
    # TC005 – Negative: empty password
    # ------------------------------------------------------------------
    {
        "test_id": "TC005_empty_password",
        "username": VALID_USERNAME,
        "password": "",
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_PASSWORD,
        "description": "Empty password — should display password error.",
        "marks": ["negative", "login"],
    },
    # ------------------------------------------------------------------
    # TC006 – Negative: both fields empty
    # ------------------------------------------------------------------
    {
        "test_id": "TC006_both_fields_empty",
        "username": "",
        "password": "",
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "Both fields empty — should display username error first.",
        "marks": ["negative", "login"],
    },
    # ------------------------------------------------------------------
    # TC007 – Security: SQL injection attempt
    # ------------------------------------------------------------------
    {
        "test_id": "TC007_sql_injection",
        "username": "' OR '1'='1' --",
        "password": "' OR '1'='1' --",
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "SQL injection in both fields — must be rejected by the app.",
        "marks": ["negative", "security", "login"],
    },
    # ------------------------------------------------------------------
    # TC008 – Security: XSS injection attempt
    # ------------------------------------------------------------------
    {
        "test_id": "TC008_xss_injection",
        "username": "<script>alert('XSS')</script>",
        "password": "<script>alert('XSS')</script>",
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "XSS payload in both fields — must be rejected by the app.",
        "marks": ["negative", "security", "login"],
    },
    # ------------------------------------------------------------------
    # TC009 – Boundary: 255-character username
    # ------------------------------------------------------------------
    {
        "test_id": "TC009_boundary_username_255_chars",
        "username": BOUNDARY_STRING_255,
        "password": VALID_PASSWORD,
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "255-char username — should be rejected.",
        "marks": ["negative", "boundary", "login"],
    },
    # ------------------------------------------------------------------
    # TC010 – Boundary: 255-character password
    # ------------------------------------------------------------------
    {
        "test_id": "TC010_boundary_password_255_chars",
        "username": VALID_USERNAME,
        "password": BOUNDARY_STRING_255,
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_PASSWORD,
        "description": "255-char password — should be rejected.",
        "marks": ["negative", "boundary", "login"],
    },
    # ------------------------------------------------------------------
    # TC011 – Negative: whitespace-only inputs
    # ------------------------------------------------------------------
    {
        "test_id": "TC011_whitespace_only_inputs",
        "username": "   ",
        "password": "   ",
        "expect_success": False,
        "expected_url_fragment": None,
        "expected_error": ERROR_INVALID_USERNAME,
        "description": "Whitespace-only credentials — should be rejected.",
        "marks": ["negative", "login"],
    },
]
