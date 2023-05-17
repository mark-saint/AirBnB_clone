#!/usr/bin/python3
"""
this is a state file
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    this is a state class
    """
    def __init__(self):
        super(State, self).__init__()
        self.name = ""
