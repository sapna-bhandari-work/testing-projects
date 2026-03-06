"""
WebDriver factory module for creating and configuring browser instances.

Supports Chrome and Firefox via WebDriver Manager, which automatically
downloads the correct driver binary for the installed browser version.
Browser selection is driven by the caller (conftest.py reads it from
CLI options, environment variables, or pytest.ini in that priority order).
"""

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

SUPPORTED_BROWSERS: tuple[str, ...] = ("chrome", "firefox")


class DriverFactory:
    """
    Factory class responsible for creating configured WebDriver instances.

    Usage::

        driver = DriverFactory.get_driver("chrome")
        driver = DriverFactory.get_driver("firefox")

    Set the ``HEADLESS=true`` environment variable to run browsers
    without a visible window (useful in CI pipelines).
    """

    @staticmethod
    def get_driver(browser: str = "chrome") -> webdriver.Remote:
        """
        Create and return a WebDriver instance for the requested browser.

        Args:
            browser: Case-insensitive browser name.  Accepted values are
                     ``'chrome'`` (default) and ``'firefox'``.

        Returns:
            A fully configured, ready-to-use Selenium WebDriver instance.

        Raises:
            ValueError: If ``browser`` is not one of the supported values.
        """
        normalised = browser.lower().strip()

        if normalised == "chrome":
            return DriverFactory._create_chrome_driver()
        if normalised == "firefox":
            return DriverFactory._create_firefox_driver()

        raise ValueError(
            f"Unsupported browser: '{browser}'. "
            f"Supported options are: {SUPPORTED_BROWSERS}"
        )

    # ------------------------------------------------------------------
    # Private builder methods
    # ------------------------------------------------------------------

    @staticmethod
    def _is_headless() -> bool:
        """Return True when the HEADLESS environment variable is 'true'."""
        return os.environ.get("HEADLESS", "false").lower() == "true"

    @staticmethod
    def _create_chrome_driver() -> webdriver.Chrome:
        """
        Build a Chrome WebDriver with sensible default options.

        Options applied:
        - ``--start-maximized``      : open browser at full screen size
        - ``--disable-notifications``: suppress browser notification prompts
        - ``--no-sandbox``           : required in some CI environments
        - ``--disable-dev-shm-usage``: prevents crashes in Docker/Linux CIs
        - ``--headless=new``         : enabled when HEADLESS env var is 'true'

        Returns:
            A configured ``selenium.webdriver.Chrome`` instance.
        """
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if DriverFactory._is_headless():
            options.add_argument("--headless=new")

        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    @staticmethod
    def _create_firefox_driver() -> webdriver.Firefox:
        """
        Build a Firefox WebDriver with sensible default options.

        Options applied:
        - ``--headless``: enabled when HEADLESS env var is 'true'

        Returns:
            A configured ``selenium.webdriver.Firefox`` instance.
        """
        options = FirefoxOptions()
        if DriverFactory._is_headless():
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        return driver
