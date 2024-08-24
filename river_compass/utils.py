"""
Module providing utility functions for solving Amazon CAPTCHA images.

Functions:
    amazon_captcha_text: Solves and returns the text from an Amazon CAPTCHA image based on its URL.
"""

from typing import Optional, Union

from amazoncaptcha import AmazonCaptcha, ContentTypeError
from requests.models import MissingSchema


def amazon_captcha_text(link: Union[str, None]) -> Optional[str]:
    """
    Solves and returns the text from an Amazon CAPTCHA image.

    Args:
        link (Union[str, None]): The URL of the CAPTCHA image.
                                 If None, the function will return None.

    Returns:
        Optional[str]: The solved CAPTCHA text if a link is provided and the CAPTCHA
                       is solved successfully. Returns None if the link is None or
                       if solving the CAPTCHA fails.
    """
    solution = None
    try:
        captcha = AmazonCaptcha.fromlink(link)
        solution = captcha.solve()
    except (MissingSchema, ContentTypeError) as error:
        print(error)
        # logger message
    return solution
