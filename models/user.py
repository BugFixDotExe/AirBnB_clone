from models.base_model import BaseModel

"""
a class User that inherits from BaseModel
Attributes:
    email: User email
    password: User password
    first_name: User first name
    last_name: User last name
"""


class User(BaseModel):
    email = None
    password = None
    first_name = None
    last_name = None
