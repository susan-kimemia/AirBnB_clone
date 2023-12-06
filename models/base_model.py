#!/usr/bin/python3
"""
This model contains the base class, parent to other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base class parent to other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes instances with neccesary attributes.
        """

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

    def save(self):
        """
        saves Instances into storage file (json file).
        """

        self.updated_at = datetime.now()
        # reinitializes object for update
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the instance which contains all
        attributes of the instance.
        """

        diction = {}
        diction["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                diction[key] = value.isoformat()
            else:
                diction[key] = value
        return diction

    def __str__(self):
        """
        returns printable string repsentation of the class instance.
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
