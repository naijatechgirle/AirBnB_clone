#!/usr/bin/python3
"""This defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Properties.

    Class Attributes:
        place_id (str): This is the Place id.
        user_id (str): This is the  User id.
        text (str): Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
