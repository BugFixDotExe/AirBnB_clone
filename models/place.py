from models.base_model import BaseModel


"""Place that represents  a place in the AirBnB properties.
Attributes:
    city_id (str): A city in the city
    user_id (str): A user Id
    name (str): The name of the state.
    description (str): It is a desciption of the place
    number_rooms (int): the number of rooms in the place
    number_bathrooms (int): The number bathrooms
    max_guest (int): the number of guest
    price_by_night(int): The price of the place
    latitude(float): the latitude
    longitude (float): the longitude
    amenity_ids (str): the list of amnety id
"""


class Place(BaseModel):

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
