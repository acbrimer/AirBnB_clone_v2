#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from models.place import Place
from models.review import Review
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable = False)
    password = Column(String(128), nullable = False)
    first_name = Column(String(128), nullable = True)
    last_name = Column(String(128), nullable = True)
    places = relationship('Place', back_populates='places')
    reviews = relationship('Review', back_populates='reviews')

    @property
    def places(self):
        from models import storage
        return { key: val for key, val in storage.all(Place).items() if val['user_id'] == self.id }
    
    @property
    def reviews(self):
        from models import storage
        return { key: val for key, val in storage.all(Review).items() if val['user_id'] == self.id }
