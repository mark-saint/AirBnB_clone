#!/usr/bin/python3
"""
this is abloody file
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    this is a class
    """
    def __init__(self):
        super(Amenity, self).__init__()
        self.name = ""
