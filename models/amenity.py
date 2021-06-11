#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128))