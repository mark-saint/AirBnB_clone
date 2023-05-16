#!/usr/bin/python3
"""
this script contains a file storage
class
"""

import json
import os


class FileStorage:
    """
    This is a file storage class
    """

    def __init__(self):
        """
        this is the __init__
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Get all the objects
        """
        return self.__objects

    def new(self, obj):
        """
        create a new object
        """
        self.__objects.update({"{}.{}".format(obj["__class__"],
                                              obj["id"]): obj})

    def save(self):
        """
        save the object
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        reload the object
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
            return self.__objects
