#!/usr/bin/python3
"""Unit test for class User"""
import unittest
import pep8
import models
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Args:
            unittest ([type]): [description]
    """

    def setUp(self):
        """Reload object"""
        self.u1 = User()
        self.u1.first_name = "Betty"
        self.u1.last_name = "Holberton"
        self.u1.email = "airbnb2@holbertonshool.com"
        self.u1.password = "root"

 
    def tearDown(self):
        """delete instance"""
        del self.u1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """test pep8"""
        fchecker = pep8.Checker('models/user.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(User.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.u1, User)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.u1.__class__, BaseModel), True)

    def test_has_attr(self):
        """Test has attr"""
        self.assertTrue('id' in self.u1.__dict__)
        self.assertTrue('created_at' in self.u1.__dict__)
        self.assertTrue('updated_at' in self.u1.__dict__)
        self.assertTrue('first_name' in self.u1.__dict__)
        self.assertTrue('last_name' in self.u1.__dict__)
        self.assertTrue('email' in self.u1.__dict__)
        self.assertTrue('password' in self.u1.__dict__)

    def test_attr_type(self):
        """Test attr_type"""
        self.assertIsInstance(self.u1.id, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)

    def test_save(self):
        """Test save"""
        before_update = self.u1.updated_at
        self.u1.save()

        self.assertNotEqual(self.u1.updated_at, before_update)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.u1), True)

if __name__ == '__main__':
    unittest.main()
