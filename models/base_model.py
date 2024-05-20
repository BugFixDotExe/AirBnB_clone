import uuid
import datetime
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
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    setattr(self, "created_at", datetime.fromisoformat(value))
                elif key == "updated_at":
                    setattr(self, "updated_at", datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of '__dict__' of the instance.
        Returns:
            dict: Dictionary representation of the instance.
        """
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        temp_dict["updated_at"] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{:s}] ({:s}) {})".format(
                self.__class__.__name__, self.id, self.__dict__
                )
