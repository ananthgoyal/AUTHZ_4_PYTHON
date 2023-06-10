#!/usr/bin/python
#-*- coding: utf-8 -*-
import Role
from Persistent import Persistent

class User(Persistent):
    """Signifies a user of the system."""
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

