"""
Module containing the CaptchaPage class, a Page Object Model for handling
the captcha page on Amazon using Selenium WebDriver.

Classes:
    CaptchaPage: Represents the Amazon captcha page and provides methods
                 to interact with the page elements, such as solving the captcha.

Methods:
    solve_captcha: Solves the captcha on the page by retrieving the captcha image,
                   extracting the text using a utility, and submitting the form.
    get_captcha_img_link: Retrieves the captcha image URL from the page.
    set_captcha: Enters the extracted captcha text into the captcha input field.
    click_submit: Clicks the submit button to validate the captcha and submit the form.
"""

from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from river_compass.utils import amazon_captcha_text


class CaptchaPage:
    """
    A Page Object Model (POM) class representing the Amazon captcha page.

    This class encapsulates the interactions with the captcha page elements such as
    the captcha image, input field, and submit button.

    Attributes:
        driver (WebDriver): Selenium WebDriver instance used to interact with the page.
        img_xpath (str): Xpath for locating the captcha image.
        input_id (str): ID for the captcha input field.
        button_class (str): Class name for the submit button.
    """

    def __init__(self, driver: WebDriver):
        """
        Initializes the CaptchaPage with a WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance used to interact with the page.
        """
        self.driver = driver
        self.img_xpath = "//div[@class='a-row a-text-center']//img"
        self.input_id = "captchacharacters"
        self.button_class = "a-button-text"

    def solve_captcha(self) -> None:
        """
        Solves the captcha on the Amazon captcha page.

        Retrieves the captcha image, extracts the text using an external utility,
        enters the extracted text into the input field, and submits the form.
        """
        captcha_link = self.get_captcha_img_link()
        captcha_txt = amazon_captcha_text(captcha_link)
        self.set_captcha(captcha_txt)
        self.click_submit()

    def get_captcha_img_link(self) -> Optional[str]:
        """
        Retrieves the captcha image URL from the page.

        Returns:
            Optional[str]: The URL of the captcha image, or None if not found.
        """
        captcha_img_link = self.driver.find_element(
            By.XPATH, self.img_xpath
        ).get_attribute("src")
        return captcha_img_link

    def set_captcha(self, captcha: Optional[str]) -> None:
        """
        Enters the captcha text into the input field.

        Args:
            captcha (Optional[str]): The captcha text to be entered.
        """
        self.driver.find_element(By.ID, self.input_id).send_keys(captcha)

    def click_submit(self) -> None:
        """
        Clicks the submit button to validate and submit the captcha form.
        """
        self.driver.find_element(By.CLASS_NAME, self.button_class).click()
