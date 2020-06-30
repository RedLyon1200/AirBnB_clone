#!/usr/bin/python3
"""Unit test for class Amenity"""
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from time import sleep
import os
import pep8
import unittest


class TestAmenity(unittest.TestCase):
    """
    Args:
            unittest ([type]): [description]
    """

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

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.a1, Amenity)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.a1.__class__, BaseModel), True)

    def test_has_attr(self):
        """Test has attr"""
        self.assertTrue('id' in self.a1.__dict__)
        self.assertTrue('created_at' in self.a1.__dict__)
        self.assertTrue('updated_at' in self.a1.__dict__)
        self.assertTrue('name' in self.a1.__dict__)

    def test_attr_type(self):
        """Test attr_type"""
        self.assertIsInstance(self.a1.id, str)
        self.assertIsInstance(self.a1.name, str)

    def test_save(self):
        """Test save"""
        before_update = self.a1.updated_at
        sleep(1.5)
        self.a1.save()

        self.assertNotEqual(self.a1.updated_at, before_update)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.a1), True)


if __name__ == '__main__':
    unittest.main()
