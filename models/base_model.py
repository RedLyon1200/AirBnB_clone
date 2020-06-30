#!/usr/bin/python3
"""This is class Base Model"""
from datetime import datetime
import json
import models
import uuid


class BaseModel:
    """class base
    """

    format_date = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """Initializing public attributes in the class
        id = contains unique identifier
        created_at = date time of object
        updated_at = update date time of object
        """

        if kwargs:
            for key, value in kwargs.items():
                if 'created_at' == key:
                    self.__dict__['created_at'] = datetime.strptime(
                        kwargs.get('created_at'), self.format_date)
                elif 'updated_at' == key:
                    self.__dict__['updated_at'] = datetime.strptime(
                        kwargs.get('updated_at'), self.format_date)
                elif '__class__' == key:
                    pass
                else:
                    self.__dict__[key] = value
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
        cpy_dict = dict(self.__dict__)
        cpy_dict['__class__'] = type(self).__name__

        for key, value in cpy_dict.items():
            if isinstance(value, datetime):
                cpy_dict[key] = value.strftime(self.format_date)

        return cpy_dict
