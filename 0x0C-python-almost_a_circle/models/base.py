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

@staticmethod
def to_json_string(dict_list):
    """convert a list of dictionaries to a JSON list
    dict_list is a list of dictionaries.
    returns JSON string represenation"""

    if not dict_list:
        return "[]"
    return json.dumps(dict_list)

@staticmethod
def from_json_string(json_string):
    """return deserialization of a json string to a list_dict"""
    if not json_string:
        return"[]"
    return json.load(json_string)
