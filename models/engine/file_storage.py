import os
import json

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
    __objects = dict()

    def all(self):
        """Return a dictionary of all objects currently stored."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary.

        Args:
            obj: The object to be added to the storage dictionary.
        """
        self.__objects["{:s}.{:s}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """
        save(self): Save the serialized objects to the JSON file.
        """        
        with open(self.__file_path, mode="w", encoding="UTF-8") as file_s:
            json.dump(self.__objects, file_s)

    def reload(self):
        """
        reload(self): Load serialized objects from the JSON file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="UTF-8") as file_s:
                pass
