#!/usr/bin/python3
""" Unittest for State class """
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

    def setUp(self):
        """SetUp method"""
        self.s1 = State()
        self.s1.name = "Agudelo"

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.s1, State)

    def test_attributes(self):
        """Test to attributes"""
        self.s1.save()
        s1_json = self.s1.to_dict()
        my_new_state = State(**s1_json)
        self.assertEqual(my_new_state.id, self.s1.id)
        self.assertEqual(my_new_state.created_at, self.s1.created_at)
        self.assertEqual(my_new_state.updated_at, self.s1.updated_at)
        self.assertIsNot(self.s1, my_new_state)

    def test_subclass(self):
        """Test to inheritance"""
        self.assertTrue(issubclass(self.s1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save"""
        variable_update = self.s1.updated_at
        self.s1.save()
        self.assertNotEqual(variable_update, self.s1.updated_at)
