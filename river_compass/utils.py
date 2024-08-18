from typing import Optional, Union

from amazoncaptcha import AmazonCaptcha


def amazon_captcha_text(link: Union[str, None]) -> Optional[str]:
    """
    Solves and returns the text from an Amazon CAPTCHA image.

    Args:
        link (str | None): The URL of the CAPTCHA image. If None, the function will return None.

    Returns:
        Optional[str]: The solved CAPTCHA text if a link is provided
                       and the CAPTCHA is solved successfully.
        Returns None if the link is None or solving fails.
    """
    if link is None:
        return None
    captcha = AmazonCaptcha.fromlink(link)
    solution = captcha.solve()
    return solution
