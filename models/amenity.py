from models.base_model import BaseModel

"""Amenity class that represents amenities available in the AirBnB properties.

    Attributes:
    id (str): Unique ID for the Amenity.
    created_at (datetime): The datetime when the Amenity
    instance was created.
    updated_at (datetime): The datetime when the Amenity
    instance was last updated.
    name (str): The name of the Amenity.
    """


class Amenity(BaseModel):
    name = ""
