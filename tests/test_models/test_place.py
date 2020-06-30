#!/usr/bin/python3
"""Unit test for class Place"""
import unittest
import pep8
import models
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Args:
            unittest ([type]): [description]
    """

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

    def test_pep8(self):
        """test pep8"""
        fchecker = pep8.Checker('models/amenity.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(Place.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.p1, Place)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.p1.__class__, BaseModel), True)

    def test_has_attr(self):
        """Test has attr"""
        self.assertTrue('id' in self.p1.__dict__)
        self.assertTrue('created_at' in self.p1.__dict__)
        self.assertTrue('updated_at' in self.p1.__dict__)
        self.assertTrue('city_id' in self.p1.__dict__)
        self.assertTrue('user_id' in self.p1.__dict__)
        self.assertTrue('name' in self.p1.__dict__)
        self.assertTrue('description' in self.p1.__dict__)
        self.assertTrue('number_rooms' in self.p1.__dict__)
        self.assertTrue('number_bathrooms' in self.p1.__dict__)
        self.assertTrue('max_guest' in self.p1.__dict__)
        self.assertTrue('price_by_night' in self.p1.__dict__)
        self.assertTrue('latitude' in self.p1.__dict__)
        self.assertTrue('longitude' in self.p1.__dict__)
        self.assertTrue('amenity_ids' in self.p1.__dict__)

    def test_attr_type(self):
        """Test attr_type"""
        self.assertIsInstance(self.p1.id, str)
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

    def test_save(self):
        """Test save"""
        before_update = self.p1.updated_at
        self.p1.save()

        self.assertNotEqual(self.p1.updated_at, before_update)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.p1), True)
