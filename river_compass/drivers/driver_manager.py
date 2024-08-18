"""Python module for having different driver manager and libraries"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class SeleniumDriverManager:
    """
    Manages Selenium WebDriver instances for various browsers.

    Attributes:
        driver_option (str): The option representing the desired browser driver.
        driver_dict (dict): A dictionary mapping driver options to corresponding methods.
    """

    def __init__(self, driver_option: str):
        """
        Initializes the SeleniumDriverManager with a specified driver option.

        Args:
            driver_option (str): The desired browser driver (e.g., "firefox").
        """
        self.driver_option = driver_option.lower()
        self.driver_dict = {"firefox": self.firefox_driver}

    def get_driver(self) -> WebDriver:
        """
        Retrieves the WebDriver instance based on the driver option.

        Returns:
            webdriver.WebDriver: An instance of the Selenium WebDriver.

        Raises:
            ValueError: If the specified driver option is not available.
        """
        if self.driver_option not in self.driver_dict:
            raise ValueError(f"Driver '{self.driver_option}' not available")

        driver_func = self.driver_dict.get(self.driver_option)
        return driver_func()

    def firefox_driver(self) -> WebDriver:
        """
        Creates and returns a headless Firefox WebDriver instance.

        Returns:
            webdriver.Firefox: An instance of the Firefox WebDriver.
        """
        service = Service(GeckoDriverManager().install())
        options = Options()
        options.add_argument("--width=2560")
        options.add_argument("--height=1440")
        driver = webdriver.Firefox(service=service, options=options)
        return driver
