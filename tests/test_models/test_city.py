#!/usr/bin/python3
""" Unittest for City class """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.city import City



class TestCity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.c1 = City()
        self.c1.state_id = "ad45ad61as6d1"
        self.c1.name = "juan"

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in"""
        self.assertIsNotNone(City.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.c1, City)

    def test_attributes(self):
        """Test to attributes"""
        self.c1.save()
        c1_json = self.c1.to_dict()
        my_new_city = City(**c1_json)
        self.assertEqual(my_new_city.id, self.c1.id)
        self.assertEqual(my_new_city.created_at, self.c1.created_at)
        self.assertEqual(my_new_city.updated_at, self.c1.updated_at)
        self.assertIsNot(self.c1, my_new_city)

    def test_subclass(self):
        """Test to inheritance"""
        self.assertTrue(issubclass(self.c1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save"""
        variable_update = self.c1.updated_at
        self.c1.save()
        self.assertNotEqual(variable_update, self.c1.updated_at)
