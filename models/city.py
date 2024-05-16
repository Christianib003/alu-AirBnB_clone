#! /usr/bin/python3
"""
This module contains the City class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents a city in the AirBnB clone project.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""