#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    def setUp(self):
        """ Set up test environment """
        pass

    def tearDown(self):
        """ Remove storage file at end of tests """
        pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        pass

    def test_new(self):
        """ New object is correctly added to __objects """
        pass

    def test_all(self):
        """ __objects is properly returned """
        pass

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        pass

    def test_empty(self):
        """ Data is saved to file """
        pass

    def test_save(self):
        """ DBStorage save method """
        pass

    def test_reload(self):
        """ Storage file is successfully loaded to db table """
        pass