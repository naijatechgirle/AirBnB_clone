#!/usr/bin/python3
"""This describes the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Properties:

    Class Attributes:
    email (str): User's email address.
    password (str): User's password.
    first_name (str): Given name of the user.
    last_name (str): Family name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
