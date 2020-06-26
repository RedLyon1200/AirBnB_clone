#!/usr/bin/python3
"""This is class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            object: [information file storage]
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Args:
            obj : key a create
        """
        FileStorage.__objects[type(self).__name__ + "." + obj.id] = obj
    
    def save(self):
        """Serialitazion of __object a json"""
        new_object = {}
        for key, value in FileStorage.__objects.items():
            new_object[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as a_file:
            json.dump(a_dict, a_file)

    def reload(self):
        a_dict = {}
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as a_file:
                a_dict = json.load(a_file)
                for key, value in a_dict.items():
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass
