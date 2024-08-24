"""
This module contains unit tests for the utility functions in the `river_compass.utils` module.

Class:
    - `TestCaptchaUtils`: Contains tests for the `amazon_captcha_text` function.

Tests:
    - `test_amazon_captcha_none_link`: Ensures the function `amazon_captcha_text` returns `None`
                                       when provided with a `None` link.
    - `test_amazon_captcha_invalid_url`: Tests that the function handles invalid URLs
                                         by returning `None`and ensures proper exception handling.
    - `test_amazon_captcha_content_type_error`: Tests that the function handles content type errors
                                                by returning `None` when AmazonCaptcha encounters
                                                invalid content.
    - `test_amazon_captcha_valid_link_str`: Tests that the function returns the correct CAPTCHA
                                            solution when a valid link is provided.
"""

from requests.exceptions import MissingSchema
from amazoncaptcha import ContentTypeError
from river_compass.utils import amazon_captcha_text


class TestCaptchaUtils:
    """
    Class to group tests for the `amazon_captcha_text` function
    in the `river_compass.utils` module.
    """

    def test_amazon_captcha_none_link(self):
        """
        Test that the function returns None when the link is None.

        This test ensures that if `amazon_captcha_text` is called with `None`,
        it returns `None`, as there is no link to process.
        """
        return_val = amazon_captcha_text(None)
        assert return_val is None

    def test_amazon_captcha_invalid_url(self, mocker):
        """
        Test that the function returns None due to exception handling
        when given an invalid URL.

        This test ensures that if `amazon_captcha_text` is called with a link
        that triggers a `MissingSchema` exception (e.g., an invalid URL),
        it returns `None`.
        """
        mocker.patch(
            "river_compass.utils.AmazonCaptcha.fromlink",
            side_effect=MissingSchema("Invalid URL"),
        )
        return_val = amazon_captcha_text("invalid_link")
        assert return_val is None

    def test_amazon_captcha_content_type_error(self, mocker):
        """
        Test that the function returns None due to ContentTypeError handling
        when AmazonCaptcha encounters invalid content.

        This test ensures that if `amazon_captcha_text` is called with a link
        that triggers a `ContentTypeError` (e.g., invalid content type),
        it returns `None`.
        """
        mocker.patch(
            "river_compass.utils.AmazonCaptcha.fromlink",
            side_effect=ContentTypeError("Invalid content"),
        )
        return_val = amazon_captcha_text("valid_link_with_invalid_content")
        assert return_val is None

    def test_amazon_captcha_valid_link_str(self, mocker):
        """
        Test that the function returns the correct CAPTCHA solution
        when a valid link is provided.

        This test ensures that if `amazon_captcha_text` is called with a valid link,
        it returns the correct CAPTCHA solution by mocking the behavior of
        `AmazonCaptcha.fromlink` and its `solve` method.
        """
        mock_fromlink = mocker.patch("river_compass.utils.AmazonCaptcha.fromlink")
        mock_captcha = mocker.MagicMock()
        mock_captcha.solve.return_value = "ABCD"
        mock_fromlink.return_value = mock_captcha
        return_val = amazon_captcha_text("valid_link")
        assert return_val == "ABCD"
