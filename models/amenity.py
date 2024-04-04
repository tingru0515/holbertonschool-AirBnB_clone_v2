#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
    This class represents Amenity
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary='place_amenity',
                                       viewonly=False,
                                       back_populates="amenities")
    else:
        name = ''