#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from models.place import Place
from sqlalchemy.orm import relationship


class City(BaseModel, Base):

    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', back_populates='places')

    @property
    def places(self):
        from models import storage
        p = storage.all(Place).items()
        return {key: val for key, val in p if val['city_id'] == self.id}
