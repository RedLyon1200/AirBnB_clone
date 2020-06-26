#!/usr/bin/python3
"""This is class Base Model"""
import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """class base
    """

    def __init__(self, *args, **kwargs):
        """Initializing public attributes in the class
        id = contains unique identifier
        created_at = date time of object
        updated_at = update date time of object
        """
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key == "__class__":
                        setattr(self, value, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns:
            [str]: [information of the class]
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Initializing de update
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns:
            a_dict: containg all information of the class
        """
        a_dict = self.__dict__
        a_dict['created_at'] = self.created_at.isoformat()
        a_dict['updated_at'] = self.updated_at.isoformat()
        a_dict['__class__'] = type(self).__name__
        return a_dict
