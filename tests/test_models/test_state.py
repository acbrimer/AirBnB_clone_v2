#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
from models import storage

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_create_state(self):
        """ Create a new state """
        new = State({"name": "Oklahoma"})
        self.assertIsNotNone(new)
    
    def test_create_state_name(self):
        new = State({"name": "California"})
        self.assertIsNotNone(new)

    def test_create_city_and_state(self):
        s = State({"name": "California"})
        storage.new(s)
        c = City({"name": "San_Francisco", "state_id": s.id})
        storage.new(c)
        self.assertIsNotNone(c)
        self.assertIsNotNone(s)
    
