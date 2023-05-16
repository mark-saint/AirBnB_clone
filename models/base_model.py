#!/usr/bin/python3
"""
This is a base file
"""


import uuid
import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        this is init
        """
        if kwargs:
            self.__dict__ = kwargs

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now().isoformat()
            self.updated_at = datetime.datetime.now().isoformat()
            storage.new(self.to_dict())

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__, (self.id),
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        BaseModel.updated_at = datetime.datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """
        returns the dict containing all keys and
        values of __dict__ of the instance
        """
        self.__dict__.update({"__class__": type(self).__name__})
        return self.__dict__
