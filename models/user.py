#! /usr/bin/python3
""" Model for the User objects """
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines the User object.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
