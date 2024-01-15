#!/usr/bin/python3
""" FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ dictionary"""
        return self.__objects

    def new(self, obj):
        """ new object """
        k_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k_name] = obj

    def save(self):
        """ save """
        from models import storage
        save_ob = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(save_ob, file)

    def reload(self):
        """ reload """
        try:
            with open(self.__file_path, 'r') as file:
                objec = json.load(file)
                for key, obj_dict in objec.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            return
