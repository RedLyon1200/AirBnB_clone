#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """class base
    """

    def __init__(self):
        """Initializing public attributes in the class
        id = contains unique identifier
        created_at = date time of object
        updated_at = update date time of object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        Returns:
            a_dict: containg all information of the class
        """
        a_dict = {}
        n_dict = dict(self.__dict__)
        for key in n_dict:
            if key == 'id':
                a_dict[key] = self.id
            elif key == 'created_at':
                a_dict[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                a_dict[key] = self.updated_at.isoformat()
        a_dict["__class__"] = type(self).__name__
        return a_dict
