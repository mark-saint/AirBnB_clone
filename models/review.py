#!/usr/bin/python3
"""
this is a file
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    this is a review class
    """
    place_id = ""
    user_id = ""
    text = ""
