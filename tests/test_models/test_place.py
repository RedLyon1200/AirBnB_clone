#!/usr/bin/python3
"""Unit test for class Place"""
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



class TestPlace(unittest.TestCase):

    def setUp(self):
        """Reload object"""
        self.p1 = Place()
        self.p1.city_id = "Medellin987"
        self.p1.user_id = "Conforte"
        self.p1.name = "Betty"
        self.p1.description = "Soleado"
        self.p1.number_rooms = 18
        self.p1.number_bathrooms = 4
        self.p1.max_guest = 245
        self.p1.price_by_night = 305678
        self.p1.latitude = 78.2
        self.p1.longitude = 108.9
        self.p1.amenity_ids = ["56deq1626", "1727132dhsad"]

    def tearDown(self):
        """delete instance"""
        del self.p1
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
        self.assertIsNotNone(Place.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.p1, Place)
        self.assertIsInstance(self.p1, BaseModel)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.p1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that all class attribute have appropriate values"""
        self.p1.save()
        p1_json = self.p1.to_dict()
        my_new_user = User(**p1_json)
        self.assertEqual(my_new_user.id, self.p1.id)
        self.assertEqual(my_new_user.created_at, self.p1.created_at)
        self.assertEqual(my_new_user.updated_at, self.p1.updated_at)
        self.assertIsNot(self.p1, my_new_user)

    def test_save(self):
        """Test save"""
        self.p1.save()
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.p1), True)


if __name__ == '__main__':
    unittest.main()
