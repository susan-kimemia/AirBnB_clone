#!/usr/bin/python3
"""
This model contains the base class for the entire project
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """base class parent to other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes instances with
        necces attribute Args"""

        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        returns printable string repsentation of the class instance.
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
