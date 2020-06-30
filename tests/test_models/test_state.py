#!/usr/bin/python3
"""Unit test for class State"""
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



class TestState(unittest.TestCase):
    """
    Args:
            unittest ([type]): [description]
    """

    def setUp(self):
        """Reload object"""
        self.s1 = State()
        self.s1.name = "Marlon"

    def tearDown(self):
        """delete instance"""
        del self.s1
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
        self.assertIsNotNone(State.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.s1, State)
        self.assertIsInstance(self.s1, BaseModel)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.s1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that all class attribute have appropriate values"""
        self.s1.save()
        s1_json = self.s1.to_dict()
        my_new_user = User(**s1_json)
        self.assertEqual(my_new_user.id, self.s1.id)
        self.assertEqual(my_new_user.created_at, self.s1.created_at)
        self.assertEqual(my_new_user.updated_at, self.s1.updated_at)
        self.assertIsNot(self.s1, my_new_user)

    def test_save(self):
        """Test save"""
        self.s1.save()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.s1), True)


if __name__ == '__main__':
    unittest.main()
