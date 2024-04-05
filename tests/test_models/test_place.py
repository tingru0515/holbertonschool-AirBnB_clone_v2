#!/usr/bin/python3
""" """
import os
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


storage_type = os.getenv("HBNB_TYPE_STORAGE")


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.args = {
            "city_id": "",
            "user_id": "",
            "name": "",
            "description": "",
            "number_rooms": 0,
            "number_bathrooms": 0,
            "max_guest": 0,
            "price_by_night": 0,
            "latitude": 0.0,
            "longitude": 0.0
        }

    def test_city_id(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(storage_type == "db", "db storage in used")
    def test_amenity_ids(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.amenity_ids), list)
