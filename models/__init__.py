#!/usr/bin/python3
"""INIT MODELS"""
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

classes = {
    'BaseModel': BaseModel,
    'State': State,
    'User': User,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}
storage = FileStorage()
storage.reload()
