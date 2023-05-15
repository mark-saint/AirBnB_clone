#!/usr/bin/python3
"""
This is a base file
"""


import uuid
import datetime
class BaseModel:

    def __init__(self):
        """
        this is init
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__, (self.id), self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        BaseModel.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        returns the dict containing all keys and values of __dict__ of the instance
        """
        return self.__dict__
