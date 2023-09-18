#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Depicts  an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Replaces in __objects obj with key <obj_class_name>.id"""
        tempName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(tempName, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        tempDict = FileStorage.__objects
        objdict = {obj: tempDict[obj].to_dict() for obj in tempDict.keys()}
        with open(FileStorage.__file_path, "w") as x:
            json.dump(objdict, x)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as x:
                objdict = json.load(x)
                for y in objdict.values():
                    clsname = o["__class__"]
                    del y["__class__"]
                    self.new(eval(clsname)(**y))
        except FileNotFoundError:
            return
