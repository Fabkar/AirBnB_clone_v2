#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Get a list of all related City current states"""
            cities = models.storage.all(City)
            listCities = []
            for classId, city in cities.items():
                if city.state_id == self.id:
                    listCities.append(city)
            return listCities
