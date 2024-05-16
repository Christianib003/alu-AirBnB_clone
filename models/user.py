#! /usr/bin/python3
""" Model for the User object """
from models.base_model import BaseModel

class User(BaseModel):
    """
    This class defines the User object.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""