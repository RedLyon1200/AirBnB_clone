#!/usr/bin/python3
"""Unit test for class Amenity"""
import unittest
import pep8
import models
from models.base_model import BaseModel
from models.review import Review
import os


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


    def test_pep8(self):
        """test pep8"""
        fchecker = pep8.Checker('models/review.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(Review.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.r1, Review)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.r1.__class__, Review), True)

    def test_has_attr(self):
        """Test has attr"""
        self.assertTrue('id' in self.r1.__dict__)
        self.assertTrue('created_at' in self.r1.__dict__)
        self.assertTrue('updated_at' in self.r1.__dict__)
        self.assertTrue('name' in self.r1.__dict__)

    def test_attr_type(self):
        """Test attr_type"""
        self.assertIsInstance(self.r1.id, str)
        self.assertIsInstance(self.r1.name, str)

    def test_save(self):
        """Test save"""
        before_update = self.r1.updated_at
        self.r1.save()

        self.assertNotEqual(self.r1.updated_at, before_update)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.r1), True)
