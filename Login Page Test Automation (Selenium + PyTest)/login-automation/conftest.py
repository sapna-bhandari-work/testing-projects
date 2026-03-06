"""
Pytest configuration module: shared fixtures and hooks for the login test suite.

Responsibilities
----------------
* Register a ``--browser`` CLI option and ``browser`` ini-option so that the
  browser can be set from the command line, an environment variable, or
  ``pytest.ini`` (in that priority order).
* Provide a ``driver`` fixture (function scope) that spins up a WebDriver
  session before each test and tears it down afterwards.
* Implement ``pytest_runtest_makereport`` to capture a screenshot whenever a
  test fails and attach it to the pytest-html report.
"""

import os
import re

import pytest

from utils.driver_factory import DriverFactory
from data.test_data import BASE_URL


# ---------------------------------------------------------------------------
# Custom CLI / ini options
# ---------------------------------------------------------------------------


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Register ``--browser`` as a command-line option and as an ini-file key.

    Priority when the ``driver`` fixture resolves the browser:
    1. ``--browser`` CLI flag
    2. ``BROWSER`` environment variable
    3. ``browser`` key in ``pytest.ini``
    4. Fallback default: ``chrome``

    Args:
        parser: The pytest argument parser provided by the framework.
    """
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser for the test run: 'chrome' (default) or 'firefox'.",
    )
    parser.addini(
        "browser",
        default="chrome",
        help="Default browser when --browser CLI flag is not supplied.",
    )


# ---------------------------------------------------------------------------
# WebDriver fixture
# ---------------------------------------------------------------------------


@pytest.fixture(scope="function")
def driver(request: pytest.FixtureRequest):
    """
    Create and yield a WebDriver instance for a single test function.

    The fixture opens ``BASE_URL`` before yielding so every test starts on
    the login page.  The browser window is closed after the test regardless
    of pass/fail outcome.

    Browser resolution order:
        1. ``--browser`` CLI argument
        2. ``BROWSER`` environment variable
        3. ``browser`` setting in ``pytest.ini``
        4. Hardcoded default: ``chrome``

    Args:
        request: The pytest ``FixtureRequest`` object for the current test.

    Yields:
        selenium.webdriver.Remote: An active WebDriver session pointed at
        ``BASE_URL``.
    """
    browser: str = (
        request.config.getoption("--browser")
        or os.environ.get("BROWSER")
        or request.config.getini("browser")
        or "chrome"
    )

    web_driver = DriverFactory.get_driver(browser)
    web_driver.get(BASE_URL)

    yield web_driver

    web_driver.quit()


# ---------------------------------------------------------------------------
# Screenshot-on-failure hook
# ---------------------------------------------------------------------------


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call):
    """
    Hook that captures a screenshot whenever a test *call* phase fails.

    Screenshots are saved to ``reports/screenshots/<sanitised_test_name>.png``.
    If the pytest-html plugin is active the image is also embedded in the
    HTML report.

    Args:
        item: The pytest test item that was just executed.
        call: The ``CallInfo`` object for the current phase.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    web_driver = item.funcargs.get("driver")
    if web_driver is None:
        return

    # ---- save screenshot to disk ----------------------------------------
    screenshot_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # Sanitise the test name so it is safe as a filename on all platforms.
    safe_name = re.sub(r"[^\w\-_.]", "_", item.name)
    screenshot_path = os.path.join(screenshot_dir, f"{safe_name}.png")

    try:
        web_driver.save_screenshot(screenshot_path)
    except Exception as exc:  # noqa: BLE001
        print(f"\n[conftest] Screenshot capture failed: {exc}")
        return

    # ---- attach to pytest-html report (if plugin is loaded) -------------
    html_plugin = item.config.pluginmanager.getplugin("html")
    if html_plugin is not None:
        extras = getattr(report, "extras", [])
        extras.append(html_plugin.extras.image(screenshot_path))
        report.extras = extras
