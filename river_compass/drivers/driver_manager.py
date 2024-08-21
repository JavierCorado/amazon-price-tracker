"""
Module providing a SeleniumDriverManager class to manage different Selenium WebDriver instances.

Classes:
    SeleniumDriverManager: Manages WebDriver instances for various
    browsers, currently supporting Firefox.

Methods:
    get_driver: Returns the appropriate WebDriver instance based on the driver option
                provided during initialization.
    firefox_driver: Creates and returns a headless Firefox WebDriver instance.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class SeleniumDriverManager:
    """
    A class to manage Selenium WebDriver instances for various browsers.

    Currently, this class supports managing a headless Firefox WebDriver.

    Attributes:
        driver_option (str): The browser option for which the WebDriver should be created.
        driver_dict (Dict[str, Callable[[], WebDriver]]): A mapping of driver options to methods
                                                          that return WebDriver instances.
    """

    def __init__(self, driver_option: str):
        """
        Initializes the SeleniumDriverManager with the specified browser option.

        Args:
            driver_option (str): The browser for which the WebDriver
            should be created (e.g., "firefox").
        """
        self.driver_option = driver_option.lower()
        self.driver_dict = {"firefox": self.firefox_driver}

    def get_driver(self) -> WebDriver:
        """
        Returns a WebDriver instance based on the provided browser option.

        The method uses the driver option to determine which WebDriver to create.
        Currently, it supports the Firefox browser.

        Returns:
            WebDriver: An instance of Selenium WebDriver.

        Raises:
            ValueError: If the driver option provided is not supported.
        """
        if self.driver_option not in self.driver_dict:
            raise ValueError(f"Driver '{self.driver_option}' not available")
        driver_func = self.driver_dict.get(self.driver_option)
        return driver_func()

    def firefox_driver(self) -> WebDriver:
        """
        Creates and returns a headless Firefox WebDriver instance.

        The WebDriver is configured with specific window dimensions for the Firefox browser.

        Returns:
            webdriver.Firefox: An instance of the Firefox WebDriver.
        """
        service = Service(GeckoDriverManager().install())
        options = Options()
        # options.add_argument("--width=2560")
        # options.add_argument("--height=1440")
        driver = webdriver.Firefox(service=service, options=options)
        return driver
