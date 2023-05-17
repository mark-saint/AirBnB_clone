#!/usr/bin/python3
"""
this is a file
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    this is a city class
    """
    super(City, self).__init__()
    self.state_id = ""
    self.name = ""
