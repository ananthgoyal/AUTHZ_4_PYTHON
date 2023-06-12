#!/usr/bin/python
#-*- coding: utf-8 -*-
import Role
from Persistent import Persistent
from datetime import datetime, date
from typing import List


class User(Persistent):
    """Signifies a user of the system."""
    name: str
    dateOfBirth: date
    roles: List[int]
    
    class Config:
        orm_mode = True


    '''
    def __init__(self, name, dateOfBirth, roles = None):
        self.name = None
        self.dateOfBirth = None
        self.roles = []

    def createSession(self, ):
        pass

    def deleteSession(self, ):
        pass

    def assignRole(self, role: Role):
        """Method to assign a user role object"""
        self.roles.append(role)

    def removeRole(self, role: Role):
        """Method to remove a role that is currently assigned to the user. Returns the associated role object"""
        #find matching role in self.roles and remove
        pass
    '''

