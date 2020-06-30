#!/usr/bin/python3
"""Unittest for class FileStorage
"""
import unittest
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""

    def setUp(self):
        """Store __objects i"""
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path

    def test_objects(self):
        """Type of __objects"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """Type of __file_path"""
        self.assertTrue(isinstance(self.file, str))

    def test_new(self):
        """Test new works"""
        model = BaseModel()
        length = len(self.objects)
        models.storage.new(model)
        self.assertTrue(length == len(self.objects))

    def test_reload(self):
        """Test reloads the object"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """Test reload reloads the object"""
        pass


class TestBaseModelFileStorage(unittest.TestCase):
    """Test BaseModel file storage"""

    def setUp(self):
        """
        Instantiate new BaseModel object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.b1 = BaseModel()
        self.b1.save()
