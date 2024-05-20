import os
import json
from datetime import datetime
import io
class FileStorage:
    """Class for storing and managing objects in a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where objects are serialized.
        __objects (dict): A dictionary to store serialized objects.

    Methods:
        all(self): Return a dictionary of all stored objects.
        new(self, obj): Add a new object to the storage dictionary.
        save(self): Save the serialized objects to the JSON file.
        reload(self): Load serialized objects from the JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary of all objects currently stored."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary.

        Args:
            obj: The object to be added to the storage dictionary.
        """
        self.__objects["{:s}.{:s}".format(obj.__class__.__name__, obj.id)] = obj


    def save(self):
        """
        save(self): Save the serialized objects to the JSON file.
        """
        # TODO: This is way too linear do make it flexible 
        dict_cpy = {}
        for key, value in self.__objects.items():
            print("##############################")

            dict_cpy["id"] = getattr(value, "id")
            print("id:", getattr(value, "id"))

            dict_cpy["created_at"] = getattr(value, "created_at").strftime("%Y-%m-%dT%H:%M:%S.%f")
            print("created_at:", getattr(value, "created_at"))

            dict_cpy["updated_at"] = getattr(value, "updated_at").strftime("%Y-%m-%dT%H:%M:%S.%f")
            print("updated_at:", getattr(value, "updated_at"))

            dict_cpy["name"] = getattr(value, "name")
            print("name:", getattr(value, "name"))

            dict_cpy["my_number"] = getattr(value, "my_number")
            print("my_number:", getattr(value, "my_number"))
            print("##############################")
        with open(self.__file_path, mode="a", encoding="UTF-8") as file_s:
            json.dump(dict_cpy, file_s)
            file_s.write("\n")

    def reload(self):
        from models.base_model import BaseModel
        """
        reload(self): Load serialized objects from the JSON file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="UTF-8") as file_s:
                for line in file_s:
                    line = io.StringIO(line)
                    to_dict = json.load(line)
                    BaseModel(**to_dict)
