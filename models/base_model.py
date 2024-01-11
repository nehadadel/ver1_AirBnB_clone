#!/usr/bin/python3
"""BaseModel"""
import models
import uuid
from datetime import datetime

class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        if kwargs:
            """ if there is arguments so we update the record """
            for un_k, data_v in kwargs.items():
                if un_k == 'created_at' or un_k == 'updated_at':
                    data_v = datetime.strptime(data_v, "%Y-%m-%dT%H:%M:%S.%f")
                elif un_k == '__class__':
                    # Skip setting '__class__' 
                    continue
                setattr(self, un_k, data_v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ string representation  """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Create a copy of the instance's dictionary """
        dic_instance = self.__dict__.copy()
        dic_instance['__class__'] = self.__class__.__name__
        dic_instance['created_at'] = self.created_at.isoformat()
        dic_instance['updated_at'] = self.updated_at.isoformat()
        return dic_instance
