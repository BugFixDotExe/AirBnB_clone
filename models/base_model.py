import uuid
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): Unique ID for the instance.
            created_at (datetime): Date and time of creation.
            updated_at (datetime): Date and time of last update.
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    setattr(self, "created_at", datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    setattr(self, "updated_at", datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "id":
                    setattr(self, "id", value)
                elif key == "name":
                    setattr(self, "name", value)
                elif key == "my_number":
                    setattr(self, "my_number", value)

    def save(self):
        """
        Updates the public instance attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of '__dict__' of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        temp_dict = self.__dict__.copy()
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        temp_dict["created_at"] = self.created_at
        temp_dict["updated_at"] = self.created_at
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{:s}] ({:s} {})".format(self.__class__.__name__,
                                         self.id, self.__dict__)
