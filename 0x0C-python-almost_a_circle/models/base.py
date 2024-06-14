#!/usr/bin/python3
class Base:
    """private attribute to keep no of instances"""
    __nb_objecs = 0
    def __init__(self, id=None)
    """constructor init takes an id argument """
        if id is not None:
            """"if id is provided its assigned directly to instance"""
            self.id = id
        else:
            """"if id is none __nb_object is incremented"""
            __nb_objects =+1
            self.id = __nb_objects
