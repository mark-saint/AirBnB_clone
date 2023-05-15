#!/usr/bin/python3
"""
This is a base file
"""


import uuid
import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        this is init
        """
        if kwargs:
            self.__dict__ = kwargs

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__, (self.id),
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        BaseModel.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns the dict containing all keys and
        values of __dict__ of the instance
        """
        return self.__dict__
