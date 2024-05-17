from models.base_model import BaseModel


 """Review an object in the AirBnB properties.

    Attributes:
    place_id (str): The place_id.
    user_id (str): The User_id
    text (str): The review of the user
    """

 class Review(BaseModel):
     place_id = ""
     user_id = ""
     text = ""
