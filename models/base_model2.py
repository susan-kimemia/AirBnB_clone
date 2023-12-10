#!/usr/bin/python3
"""
The model contains the base class for the entire project
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """base class source to other classes"""


def save(self):

    self.updated_at = datetime.now()
    models.storage.new(self)
    models.storage.save()


def to_dict(self):

    obj_diction = {}
    obj_diction["__class__"] = self.__class__.__name__

    for key, value in self.__dict__.items():
        if isinstance(value, datetime):
            obj_diction[key] = value.isoformat()
        else:
            obj_diction[key] = value
    return obj_diction
