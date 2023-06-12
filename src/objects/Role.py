#!/usr/bin/python
#-*- coding: utf-8 -*-

from typing import List
from src.objects.Persistent import Persistent
#from pydantic import BaseModel


class Role(Persistent):
    """Is an organized set of permissions intended to reflect an organization function."""
    name: str = "" #Name of the Role
    permissions: List[int] = [] #List of all unique Int ID's of permssions the role contains
    tags: List[str] = [] #List of strings indicating all associated tags with role

    class Config:
        orm_mode = True

    def addPermission(self, permission):
        """Adds a permission to the set"""
        pass

    def remPermission(self, permission):
        """Removes a permission from a the set"""
        pass

    def addTag(self, tag):
        """Adds a tag to the tag set"""

    def remTag(self, tag):
        """Removes a tag from the tag set if that tag is present"""

