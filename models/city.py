#!/usr/bin/python3
"""This defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Properties:

    Class Attributes:
        state_id (str): This is the state id.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
