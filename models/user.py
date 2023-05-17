#!/usr/bin/python3
"""
this is a bloody file
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    this is a user class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
