"""
Module defining the ArticlePage class for interacting with product pages
on a website using Selenium WebDriver.

Classes:
    ArticlePage: Represents a product page and provides methods to retrieve
    the product name and price.

Methods:
    get_name: Retrieves the name of the product from the page.
    get_price: Retrieves the price of the product from the page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ArticlePage:
    """
    A Page Object Model (POM) class for interacting with a product page.

    This class provides methods to access the product's name and price on the page.

    Attributes:
        driver (WebDriver): Selenium WebDriver instance used to interact with the page.
        name_id (str): The ID of the HTML element containing the product name.
        price_xpath (str): The XPath of the HTML element containing the product price.
    """

    def __init__(self, driver: WebDriver):
        """
        Initializes the ArticlePage with a WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance used to interact with the page.
        """
        self.driver = driver
        self.name_id = "productTitle"
        self.price_xpath = (
            "//span[contains(@class, 'a-price') and "
            "contains(@class, 'aok-align-center') and "
            "contains(@class, 'reinventPricePriceToPayMargin') and "
            "contains(@class, 'priceToPay')]//span[@aria-hidden='true']"
        )

    def get_name(self) -> str:
        """
        Retrieves the name of the product from the page.

        Returns:
            str: The name of the product as displayed on the page.
        """
        article_name = self.driver.find_element(By.ID, self.name_id).text
        return article_name

    def get_price(self) -> str:
        """
        Retrieves the price of the product from the page.

        Returns:
            str: The price of the product as displayed on the page.
        """
        article_price = self.driver.find_element(By.XPATH, self.price_xpath).text
        return article_price
