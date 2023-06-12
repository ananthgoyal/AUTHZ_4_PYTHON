#!/usr/bin/python
#-*- coding: utf-8 -*-

from typing import List
from src.Persistent import Persistent
#from pydantic import BaseModel


class Role(Persistent):
    """Is an organized set of permissions intended to reflect an organization function."""
    name: str
    permissions: List
    tags: List

    class Config:
        orm_mode = True

    def addPermission(self, permission):
        """Adds a permission to the set"""
        pass

    def remPermission(self, permission):
        """Removes a permission from a the set"""
        pass

    def addTag(self, String):
        pass

