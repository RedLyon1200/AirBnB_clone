#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """class base
    """

    def __init__(self, name=None, my_number=0):
        """Initializing public attributes in the class
        id = contains unique identifier
        created_at = date time of object
        updated_at = update date time of object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if name:
            self.name = name
        if my_number:
            self.my_number = my_number

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
        for key in self.__dict__:
            if key == 'id':
                a_dict[key] = self.id
            elif key == 'created_at':
                a_dict[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                a_dict[key] = self.updated_at.isoformat()
            
        a_dict["__class__"] = type(self).__name__
        return a_dict
