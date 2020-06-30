#!/usr/bin/python3
"""Unit test for class BaseModel"""
from contextlib import redirect_stdout
from datetime import datetime
import io
import models
from models.base_model import BaseModel
import pep8
import unittest
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Class TestBaseModels:
                    unittest (unittes): [test of my class basemodels]
    """
    name = "Holberton"
    my_number = 45

    def setUp(self):
        """Reload object"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_pep8(self):
        """test pep8"""
        fchecker = pep8.Checker('models/base_model.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id(self):
        """Test unique id for objects"""
        self.assertTrue(type(self.b1.id) is str)
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_date_type(self):
        """Test type created_at and update_at is datetime"""
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_instance(self):
        """Test instance of BaseModel"""
        self.assertIsInstance(self.b1, BaseModel)

    def test_new_attr(self):
        """Test create new attribute"""
        self.b1.name = self.name
        self.b1.my_number = self.my_number
        self.assertEqual(self.b1.name, self.name)
        self.assertEqual(self.b1.my_number, self.my_number)

    def test_keyward(self):
        """Test keyward in the objects"""
        b1_dict = self.b1.to_dict()
        b3 = BaseModel(**b1_dict)
        b3_dict = b3.to_dict()
        self.assertIsInstance(b3, BaseModel)
        self.assertTrue(b3.id is self.b1.id)
        self.assertEqual(b3_dict['created_at'], b1_dict['created_at'])
        self.assertEqual(b3_dict['updated_at'], b1_dict['updated_at'])

    def test_str(self):
        """Test str print"""
        file = io.StringIO()
        output = "[{}] ({}) {}\n".format(
            type(self.b1).__name__, self.b1.id, self.b1.__dict__)
        with redirect_stdout(file):
            print(self.b1)
        self.assertEqual(output, file.getvalue())

    def test_save(self):
        """Test save update date"""
        before_update = self.b1.updated_at
        sleep(1.5)
        self.b1.save()
        self.assertNotEqual(before_update, self.b1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.b1.name = self.name
        self.b1.my_number = self.my_number
        b1_dict = self.b1.to_dict()

        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertEqual(b1_dict['id'], self.b1.id)
        create_it = b1_dict['created_at'].split('T')
        self.assertEqual(" ".join(create_it), str(self.b1.created_at))
        update_it = b1_dict['updated_at'].split('T')
        self.assertEqual(" ".join(update_it), str(self.b1.updated_at))
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
        self.assertIsInstance(b1_dict['name'], str)
        self.assertIsInstance(b1_dict['my_number'], int)


if __name__ == '__main__':
    unittest.main()
