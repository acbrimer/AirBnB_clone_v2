#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE', '') == 'db':
        cities = relationship('City', back_populates='cities')
    else:
        @property
        def cities(self):
            from models import storage
            c = storage.all(City).values()
            return [obj for obj in c if obj.state_id == self.id]
