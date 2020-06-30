#!/usr/bin/python3
"""Unit test for class User"""
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


class TestUser(unittest.TestCase):

    def setUp(self):
        """setup instance"""
        self.u1 = User()
        self.u1.first_name = "Betty"
        self.u1.last_name = "Holberton"
        self.u1.email = "airbnb@holbertonshool.com"
        self.u1.password = "root"

    def tearDown(self):
        """delete instance"""
        del self.u1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.u1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that all class attribute have appropriate values"""
        self.u1.save()
        u1_json = self.u1.to_dict()
        my_new_user = User(**u1_json)
        self.assertEqual(my_new_user.id, self.u1.id)
        self.assertEqual(my_new_user.created_at, self.u1.created_at)
        self.assertEqual(my_new_user.updated_at, self.u1.updated_at)
        self.assertIsNot(self.u1, my_new_user)

    def test_attribute_type(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.u1, User)
        self.assertIsInstance(self.u1, BaseModel)
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        """check docstrings for existing functions"""
        self.u1.save()
        self.assertNotEqual(self.u1.created_at, self.u1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.u1), True)

if __name__ == '__main__':
    unittest.main()
