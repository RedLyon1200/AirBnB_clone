#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity



class TestAmenity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.a1 = Amenity()
        self.a1.name = "juan"

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_is_instance(self):
        """Test instantiation"""
        self.assertIsInstance(self.a1, Amenity)

    def test_attributes(self):
        """Test to check attributes"""
        self.a1.save()
        a1_json = self.a1.to_dict()
        my_new_amenity = Amenity(**a1_json)
        self.assertEqual(my_new_amenity.id, self.a1.id)
        self.assertEqual(my_new_amenity.created_at, self.a1.created_at)
        self.assertEqual(my_new_amenity.updated_at, self.a1.updated_at)
        self.assertIsNot(self.a1, my_new_amenity)

    def test_subclass(self):
        """Test to inheritance"""
        self.assertTrue(issubclass(self.a1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save"""
        variable_update = self.a1.updated_at
        self.a1.save()
        self.assertNotEqual(variable_update, self.a1.updated_at)
