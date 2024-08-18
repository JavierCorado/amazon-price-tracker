"""Python module for the article pydantic model"""

from typing import Optional

from pydantic import BaseModel, Field


class Article(BaseModel):
    """
    A model representing an article.

    Attributes:
        name (str): The name of the article.
        price (float): The price of the article.
        description (Optional[str]): An optional description of the article.
    """

    name: str = Field(..., description="The name of the article.")
    price: float = Field(..., description="The price of the article.")
    description: Optional[str] = Field(
        None, description="An optional description of the article."
    )
