#!/usr/bin/python3
"""
this is a bloody file
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    this is a user class
    """
    def __init__(self):
        super(User, self).__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
