#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id')),
    Column('amenity_id', String(60), ForeignKey('amenities.id'))
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable = False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable = False)
    name = Column(String(128), nullable = False)
    description = Column(String(1024), nullable = True)
    number_rooms = Column(Integer, nullable = False, default=0)
    number_bathrooms = Column(Integer, nullable = False, default=0)
    max_guest = Column(Integer, nullable = False, default=0)
    price_by_night = Column(Integer, nullable = False, default=0)
    latitude = Column(Float, nullable = True)
    longitude = Column(Float, nullable = True)
    reviews = relationship('Review', back_populates='reviews')
    amenities = relationship('Amenity',
                    viewonly=False,
                    secondary=place_amenity,
                    backref='amenities')
    amentity_ids = []

    @property
    def reviews(self):
        from models import storage
        return { key: val for key, val in storage.all(Review).items() if val['user_id'] == self.id }

    @property
    def amenities(self):
        from models import storage
        return { key: val for key, val in storage.all(Amenity).items() if val['id'] in self.amentity_ids }
    
    @amenities.setter
    def amenities(self, val):
        self.amentity_ids.append(val)