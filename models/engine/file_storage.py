import os

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

    __file_path = None
    __objects = dict()

    def all(self):
        """Return a dictionary of all objects currently stored."""

        print("Well this is rather fitting.")
    def new(self, obj):
        """Add a new object to the storage dictionary.

        Args:
            obj: The object to be added to the storage dictionary.
        """
        pass

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
        if os.path.exist(self.__file_path):
            with open(self.__file_path, mode="r", encoding="UTF-8") as file_s:
                self.__objects = dict(json.load(file_s)).copy()
