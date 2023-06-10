#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persistent import Persistent

class Role(Persistent):
    """Is an organized set of permissions intended to reflect an organization function."""
    def __init__(self):
        self.name = None
        self.permissions = None
        self.tags = None

    def addPermission(self, Permission):
        """Adds a permission to the set"""
        pass

    def remPermission(self, Permission):
        """Removes a permission from a the set"""
        pass

    def addTag(self, String):
        pass

