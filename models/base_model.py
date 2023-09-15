#!/usr/bin/python3
"""This defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """This initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        yform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, yform)
                else:
                    self.__dict__[a] = b
        else:
            models.storage.new(self)

    def save(self):
        """This updates updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This returns the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        ydict = self.__dict__.copy()
        ydict["created_at"] = self.created_at.isoformat()
        ydict["updated_at"] = self.updated_at.isoformat()
        ydict["__class__"] = self.__class__.__name__
        return ydict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)
