#!/usr/bin/python3
"""Unittest for class FileStorage
"""
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pep8
from os import remove
import unittest


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""

    def setUp(self):
        """Stores __objects in variables for easy use in test cases"""
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path

    def tearDown(self):
        """delete JSON file"""
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """test pep8"""
        fchecker = pep8.Checker(
            'models/engine/file_storage.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)
    
    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_objects(self):
        """Type of __objects"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """Type of __file_path"""
        self.assertTrue(isinstance(self.file, str))

    def test_new(self):
        """Test new works"""
        model = BaseModel()
        length = len(self.objects)
        models.storage.new(model)
        self.assertTrue(length == len(self.objects))

    def test_reload(self):
        """Reloads the object"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """Reloads the object"""
        self.assertTrue(isinstance(self.objects, dict))


class TestBaseModelFileStorage(unittest.TestCase):
    """Test BaseModel file storage"""

    def setUp(self):
        """
        Instantiate new BaseModel object and store data
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.b1 = BaseModel()
        self.b1.save()

    def tearDown(self):
        """delete instance"""
        del self.b1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_basemodel_object_update(self):
        """Try adding new objects"""
        self.assertIn('BaseModel.{}'.format(self.b1.id), self.objects.keys())
    
    def test_fs_instance(self):
        """FileStorage class save checks, reload checks"""
        b1 = BaseModel()
        models.storage.save()
        self.assertEqual(os.path.exists('file.json'), True)

    def test_basemodel_dict(self):
        """Test if new data is added to __objects"""
        b1_dict = self.b1.to_dict()
        for value in self.objects.values():
            self.assertTrue(value, b1_dict)


class TestUserFileStorage(unittest.TestCase):
    """Test User file storage"""

    def setUp(self):
        """Test whether new User objects get added to __objects"""

        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.u1 = User()
        self.u1.save()
        self.assertIn('User.{}'.format(self.u1.id), self.objects.keys())

    def tearDown(self):
        """delete instance"""
        del self.u1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_dict(self):
        """Test whether new User objects' dicts get added to __objects"""
        u1_dict = self.u1.to_dict()
        """ self.assertIn(u1_dict, self.objects.values()) """
        for value in self.objects.values():
            self.assertTrue(value, u1_dict)


class TestStateFileStorage(unittest.TestCase):
    """Test State file storage"""

    def setUp(self):
        """
        Instantiate new State object and store data
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.s1 = State()
        self.s1.save()

    def tearDown(self):
        """delete instance"""
        del self.s1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_state_object_update(self):
        """Test whether new State objects get added to __objects"""
        self.assertIn('State.{}'.format(self.s1.id), self.objects.keys())

    def test_state_dict(self):
        """Test whether new State objects' dicts get added to __objects"""
        s1_dict = self.s1.to_dict()

        """ self.assertIn('create_at', s1_dict) """
        for value in self.objects.values():
            self.assertTrue(value, s1_dict)


class TestCityFileStorage(unittest.TestCase):
    """Test City file storage"""

    def setUp(self):
        """
        Instantiate new City object and store data
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.c1 = City()
        self.c1.save()

    def tearDown(self):
        """delete instance"""
        del self.c1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_city_object_update(self):
        """Test whether new City objects get added to __objects"""
        self.assertIn('City.{}'.format(self.c1.id), self.objects.keys())

    def test_city_dict(self):
        """Test whether new City objects' dicts get added to __objects"""
        c1_dict = self.c1.to_dict()
        """ self.assertIn(c1_dict, self.objects.values()) """
        for value in self.objects.values():
            self.assertTrue(value, c1_dict)


class TestAmenityFileStorage(unittest.TestCase):
    """Test Amenity file storage"""

    def setUp(self):
        """
        Instantiate new Amenity object and store data
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.a1 = Amenity()
        self.a1.save()

    def tearDown(self):
        """delete instance"""
        del self.a1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_amenity_object_update(self):
        """Test whether new Amenity objects get added to __objects"""
        self.assertIn('Amenity.{}'.format(self.a1.id), self.objects.keys())

    def test_amenity_dict(self):
        """Test whjether new Amenity objects' dicts get added to __objects"""
        a1_dict = self.a1.to_dict()
        """ self.assertIn(a1_dict, self.objects.values()) """
        for value in self.objects.values():
            self.assertTrue(value, a1_dict)


class TestPlaceFileStorage(unittest.TestCase):
    """Test Place file storage"""

    def setUp(self):
        """
        Instantiate new Place object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.p1 = Place()
        self.p1.save()

    def tearDown(self):
        """delete instance"""
        del self.p1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_place_object_update(self):
        """Test whether new Place objects get added to __objects"""
        self.assertIn('Place.{}'.format(self.p1.id), self.objects.keys())

    def test_place_dict(self):
        """Test whether new Place objects' dicts get added to __objects"""
        p1_dict = self.p1.to_dict()
        for value in self.objects.values():
            self.assertTrue(value, p1_dict)
        """ self.assertIn(p1_dict, self.objects.values()) """


class TestReviewFileStorage(unittest.TestCase):
    """Test Review file storage"""

    def setUp(self):
        """
        Instantiate new Review object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file = FileStorage._FileStorage__file_path
        self.r1 = Review()
        self.r1.save()

    def tearDown(self):
        """delete instance"""
        del self.r1
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_review_object_update(self):
        """Test whether new Review objects get added to __objects"""
        self.assertIn('Review.{}'.format(self.r1.id), self.objects.keys())

    def test_review_dict(self):
        """Test whether new Review objects' dicts get added to __objects"""
        r1_dict = self.r1.to_dict()
        for value in self.objects.values():
            self.assertTrue(value, r1_dict)
        """ self.assertIn(r1_dict, self.objects.values()) """


if __name__ == '__main__':
    unittest.main()
