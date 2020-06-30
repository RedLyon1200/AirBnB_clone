#!/usr/bin/python3
"""Unit test for class Amenity"""
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage



class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Reload object"""
        self.a1 = Amenity()
        self.a1.name = "Deiwin"

    def tearDown(self):
        """delete instance"""
        del self.a1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.a1, Amenity)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.a1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that all class attribute have appropriate values"""
        self.a1.save()
        a1_json = self.a1.to_dict()
        my_new_user = User(**a1_json)
        self.assertEqual(my_new_user.id, self.a1.id)
        self.assertEqual(my_new_user.created_at, self.a1.created_at)
        self.assertEqual(my_new_user.updated_at, self.a1.updated_at)
        self.assertIsNot(self.a1, my_new_user)


    def test_save(self):
        """Test save"""
        self.a1.save()
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.a1), True)


if __name__ == '__main__':
    unittest.main()
