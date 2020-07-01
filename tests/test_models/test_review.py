#!/usr/bin/python3
""" Unittest for Review class """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.review import Review



class TestReview(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.r1 = Review()
        self.r1.place_id = "carenha"
        self.r1.user_id = "3r45t9s323d9"
        self.r1.text = "Elteso"

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.r1, Review)

    def test_attributes(self):
        """Test to attributes"""
        self.r1.save()
        r1_json = self.r1.to_dict()
        my_new_review = Review(**r1_json)
        self.assertEqual(my_new_review.id, self.r1.id)
        self.assertEqual(my_new_review.created_at, self.r1.created_at)
        self.assertEqual(my_new_review.updated_at, self.r1.updated_at)
        self.assertIsNot(self.r1, my_new_review)

    def test_subclass(self):
        """Test to inheritance"""
        self.assertTrue(issubclass(self.r1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save"""
        variable_update = self.r1.updated_at
        self.r1.save()
        self.assertNotEqual(variable_update, self.r1.updated_at)
