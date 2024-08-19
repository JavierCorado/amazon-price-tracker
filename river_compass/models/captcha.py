"""Python module with Amazon captcha Page Object Model"""


class CaptchaPage:
    def __init__(self, driver):
        self.img_xpath = "//div[@class='a-row a-text-center']//img"
        self.input_id = "captchacharacters"
        self.button_class = "a-button-text"
        self.driver = driver
