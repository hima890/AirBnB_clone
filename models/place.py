#!/usr/bin/python3
"""
class named place that inharits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from BaseModel class

     Attributes:
        city_id (string): the City id
        user_id (string): the User id
        name (string): the name of the place.
        description (str): the description of the place
        number_rooms (int):the  number of rooms of the place
        number_bathrooms (int):the  number of bathrooms of the place
        max_guest (int):the  maximum number of guests of the place
        price_by_night (int): the price by night of the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): the list of Amenity ids

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
