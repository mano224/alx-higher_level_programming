#!/usr/bin/python3
'''contains the class "student"'''

class student:
    '''Representation of a student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        '''return a dictionary representaion of a student instance'''
        return self.__dict__

