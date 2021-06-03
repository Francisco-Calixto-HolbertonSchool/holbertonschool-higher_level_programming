#!/usr/bin/python3
"""This module contains Square class"""


class Student():
    """Square class inherits from Rectangle"""

    def __init__(self, first_name, last_name, age):
        """instantiation with full name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            if all(type(el) is str for el in attrs):
                dic2 = {}
                for i in attrs:
                    if i in self.__dict__:
                        dic2[i] = self.__dict__[i]
                return (dic2)
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """public method: replaces all attributs of the Student ins"""
        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]
