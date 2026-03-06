"""
Page Object Model for the Login Page of the-internet.herokuapp.com.

Encapsulates all locators and user interactions so that test code
remains decoupled from page implementation details.
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """
    Represents the login page at https://the-internet.herokuapp.com/login.

    All element locators live here.  Tests interact with the page only
    through the public methods below, never through raw Selenium calls.
    """

    URL: str = "https://the-internet.herokuapp.com/login"

    # ------------------------------------------------------------------
    # Locators
    # ------------------------------------------------------------------
    _USERNAME_FIELD = (By.ID, "username")
    _PASSWORD_FIELD = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _FLASH_MESSAGE = (By.ID, "flash")

    _DEFAULT_TIMEOUT: int = 10

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------
    def __init__(self, driver: WebDriver) -> None:
        """
        Initialise the LoginPage with a WebDriver instance.

        Args:
            driver: An active Selenium WebDriver session.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self._DEFAULT_TIMEOUT)

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------
    def open(self) -> "LoginPage":
        """
        Navigate the browser to the login page URL.

        Returns:
            Self, to allow method chaining.
        """
        self.driver.get(self.URL)
        return self

    # ------------------------------------------------------------------
    # Input actions
    # ------------------------------------------------------------------
    def enter_username(self, username: str) -> "LoginPage":
        """
        Clear the username field and type the supplied value.

        Args:
            username: The username string to enter (may be empty).

        Returns:
            Self, to allow method chaining.
        """
        field = self.wait.until(
            EC.visibility_of_element_located(self._USERNAME_FIELD)
        )
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """
        Clear the password field and type the supplied value.

        Args:
            password: The password string to enter (may be empty).

        Returns:
            Self, to allow method chaining.
        """
        field = self.wait.until(
            EC.visibility_of_element_located(self._PASSWORD_FIELD)
        )
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self) -> "LoginPage":
        """
        Click the login submit button.

        Returns:
            Self, to allow method chaining.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        )
        button.click()
        return self

    # ------------------------------------------------------------------
    # Composite action
    # ------------------------------------------------------------------
    def login(self, username: str, password: str) -> "LoginPage":
        """
        Perform a complete login: enter username, enter password, click login.

        Args:
            username: The username to submit.
            password: The password to submit.

        Returns:
            Self, to allow method chaining.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    # ------------------------------------------------------------------
    # Assertions / query helpers
    # ------------------------------------------------------------------
    def get_flash_message(self) -> str:
        """
        Wait for and return the full text of the flash message element.

        The flash element is used for both success and error messages on
        this demo site.

        Returns:
            The stripped text content of the flash message.

        Raises:
            TimeoutException: If the flash element does not appear within
                              the configured timeout.
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self._FLASH_MESSAGE)
        )
        return element.text.strip()

    def get_error_message(self) -> str:
        """
        Return the flash message text, expected to contain an error.

        This is a semantic alias for ``get_flash_message`` to improve
        test readability when a failure outcome is expected.

        Returns:
            The stripped text content of the flash message.
        """
        return self.get_flash_message()

    def is_error_displayed(self) -> bool:
        """
        Check whether the flash message element is currently visible.

        Returns:
            True if the flash message element is visible, False otherwise.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self._FLASH_MESSAGE)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def is_login_button_visible(self) -> bool:
        """
        Check whether the login button is currently visible on the page.

        Returns:
            True if the login button is visible, False otherwise.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self._LOGIN_BUTTON)
            )
            return element.is_displayed()
        except TimeoutException:
            return False
