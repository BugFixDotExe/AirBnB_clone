import uuid
import datetime
import time

class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    #setattr(self, "created_at", "asdsadas")
                    self.created_at = time.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = time.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                elif key == "id":
                    self.id = value
                elif key == "name":
                    self.name = value
                elif key == "my_number":
                    self.my_number = value

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        setattr(self, "created_at", self.created_at)
        setattr(self, "updated_at", self.created_at)
        self.__dict__["__class__"] = self.__class__.__name__
        # setattr(self, str(self.__str__), self.__class__.__name__)
        return self.__dict__

    def __str__(self):
        return "[{:s}] ({:s} {})".format(self.__class__.__name__,
                                         self.id, self.__dict__)
