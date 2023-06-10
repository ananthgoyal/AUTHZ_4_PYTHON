#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persistent import Persistent

class Permission(Persistent):
    """
    Permissions specify what tasks users can perform and what features users can access.

    Note: As of now (for simplicity), the design of the permissions class has type as an attribute but will later be adjusted to be an abstract class with unique permission types as children objects.
    """
    def __init__(self):
        self.type = None
        self.type = None
        self.canRead = None
        self.canCreate = None
        self.canDelete = None
        self.isRequired = None
        self.isEnabled = None
        self.canReadAll = None
        self.canAssign = None
        self.canShare = None
        self.canUpdate = None

