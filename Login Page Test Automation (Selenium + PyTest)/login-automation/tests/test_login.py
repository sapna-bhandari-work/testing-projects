"""
Test module for the login page of https://the-internet.herokuapp.com/login.

All test cases are driven by the ``TEST_SCENARIOS`` list defined in
``data/test_data.py``.  Each scenario is executed as an independent,
parametrized test function so failures are isolated and reported individually.

Test IDs in the parametrize list match the ``test_id`` field of each
scenario dict, making it straightforward to re-run a single case with::

    pytest -k TC007_sql_injection
"""

import pytest

from pages.login_page import LoginPage
from data.test_data import TEST_SCENARIOS


# ---------------------------------------------------------------------------
# Build the parametrize argument list
# ---------------------------------------------------------------------------

_MARK_REGISTRY: dict[str, pytest.MarkDecorator] = {
    "login": pytest.mark.login,
    "positive": pytest.mark.positive,
    "negative": pytest.mark.negative,
    "security": pytest.mark.security,
    "boundary": pytest.mark.boundary,
}


def _build_marks(scenario: dict) -> list[pytest.MarkDecorator]:
    """
    Convert the scenario's ``marks`` list into pytest mark objects.

    Args:
        scenario: A single scenario dict from ``TEST_SCENARIOS``.

    Returns:
        A list of ``pytest.MarkDecorator`` objects ready to attach to a
        ``pytest.param``.
    """
    return [
        _MARK_REGISTRY[name]
        for name in scenario.get("marks", [])
        if name in _MARK_REGISTRY
    ]


_PARAM_LIST: list[pytest.param] = [
    pytest.param(
        scenario,
        id=scenario["test_id"],
        marks=_build_marks(scenario),
    )
    for scenario in TEST_SCENARIOS
]


# ---------------------------------------------------------------------------
# Test class
# ---------------------------------------------------------------------------


class TestLogin:
    """
    Test suite covering all login scenarios defined in ``data/test_data.py``.

    Each parametrized invocation exercises one combination of inputs and
    verifies the expected outcome — either a successful redirect or a
    correctly rendered error message.
    """

    @pytest.mark.login
    @pytest.mark.parametrize("scenario", _PARAM_LIST)
    def test_login_scenario(self, driver, scenario: dict) -> None:
        """
        Execute one login scenario end-to-end and assert the expected outcome.

        For **success** scenarios (``expect_success=True``):
        - Asserts the current URL contains the secure-area fragment.

        For **failure** scenarios (``expect_success=False``):
        - Asserts the error flash element is visible.
        - Asserts the flash text contains the expected error substring.
        - Asserts the URL has **not** changed to the secure area.

        Args:
            driver: Selenium WebDriver fixture provided by ``conftest.py``.
            scenario: A single scenario dict from ``TEST_SCENARIOS``.
        """
        test_id: str = scenario["test_id"]
        page = LoginPage(driver)

        # Navigate to the login page and submit credentials
        page.open()
        page.login(scenario["username"], scenario["password"])

        if scenario["expect_success"]:
            # ----------------------------------------------------------
            # Positive path: successful login → redirect to /secure
            # ----------------------------------------------------------
            expected_fragment: str = scenario["expected_url_fragment"]
            actual_url: str = driver.current_url

            assert expected_fragment in actual_url, (
                f"[{test_id}] Expected URL to contain '{expected_fragment}', "
                f"but got: '{actual_url}'"
            )

        else:
            # ----------------------------------------------------------
            # Negative path: login should fail with an error message
            # ----------------------------------------------------------

            # Assertion 1 – error element is visible on the page
            assert page.is_error_displayed(), (
                f"[{test_id}] Expected an error message to be displayed on "
                "the page, but the flash element was not found or not visible."
            )

            # Assertion 2 – error text matches the expected substring
            expected_error: str = scenario["expected_error"]
            actual_error: str = page.get_error_message()

            assert expected_error in actual_error, (
                f"[{test_id}] Expected error message to contain "
                f"'{expected_error}', but got: '{actual_error}'"
            )

            # Assertion 3 – URL has NOT advanced to the secure area
            actual_url = driver.current_url
            assert "/secure" not in actual_url, (
                f"[{test_id}] Login should have failed but the browser "
                f"navigated to a secured page: '{actual_url}'"
            )
