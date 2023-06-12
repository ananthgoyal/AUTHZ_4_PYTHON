#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.Persistent import Persistent

class Permission(Persistent):
    """
    Permissions specify what tasks users can perform and what features users can access.

    Note: As of now (for simplicity), the design of the permissions class has type as an attribute but will later be adjusted to be an abstract class with unique permission types as children objects.
    """
    can_create: bool
    can_update: bool
    can_delete: bool
    can_read: bool
    can_read_all: bool
    can_assign: bool
    can_share: bool

    class Config:
        orm_mode = True
