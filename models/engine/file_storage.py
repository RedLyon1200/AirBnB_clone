#!/usr/bin/python3
"""This is class self"""
import models
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
import json
import os.path as path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to \
    instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        Returns:
            __object dictionary
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (obj): object
        """
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        a_dict = {}
        for key in self.__objects:
            a_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w",
                  encoding="utf-8") as a_file:
            json.dump(a_dict, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r",
                      encoding="utf-8") as a_file:
                    a_dict = json.load(a_file)
                    for key, value in a_dict.items():
                        if value.get('__class__') in models.classes:
                            methd = value.get('__class__')
                            FileStorage.__objects[key] = eval(methd)(**value)
