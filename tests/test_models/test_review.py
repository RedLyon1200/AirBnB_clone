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



class TestReview(unittest.TestCase):
    """
    Args:
            unittest ([type]): [description]
    """

    def setUp(self):
        """Reload object"""
        self.r1 = Review()
        self.r1.name = "Deiwin"

    def tearDown(self):
        """delete instance"""
        del self.r1
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
        self.assertIsNotNone(Review.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.r1, Review)
        self.assertIsInstance(self.r1, BaseModel)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.r1.__class__, Review), True)

    def test_has_attributes(self):
        """check that all class attribute have appropriate values"""
        self.r1.save()
        r1_json = self.r1.to_dict()
        my_new_user = User(**r1_json)
        self.assertEqual(my_new_user.id, self.r1.id)
        self.assertEqual(my_new_user.created_at, self.r1.created_at)
        self.assertEqual(my_new_user.updated_at, self.r1.updated_at)
        self.assertIsNot(self.r1, my_new_user)

    def test_attr_type(self):
        """Test attr_type"""
        self.assertIsInstance(self.r1.name, str)

    def test_save(self):
        """Test save"""
        self.r1.save()
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.r1), True)


if __name__ == '__main__':
    unittest.main()
