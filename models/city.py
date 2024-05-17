from models.base_model import BaseModel

 """
 City class that represents states in the AirBnB properties.

    Attributes:
    name (str): The name of the city.
    state_id(str): The ID of the City
 """

class City(BaseModel):
    state_id = ""
    name = ""
