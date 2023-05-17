#!/usr/bin/python3
"""
this is a file
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    this is a review class
    """
    def __init__(self):
        super(Review, self).__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
