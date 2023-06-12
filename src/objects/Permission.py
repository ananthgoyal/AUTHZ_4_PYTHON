#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.objects.Persistent import Persistent

class Permission(Persistent):
    """
    Permissions specify what tasks users can perform and what features users can access.

    Note: As of now (for simplicity), the design of the permissions class has type as an attribute but will later be adjusted to be an abstract class with unique permission types as children objects.
    """
    can_create: bool = False #Whether user can create
    can_update: bool = False #Whether user can update
    can_delete: bool = False #Whether user can delete
    can_read: bool = False #Whether user can read
    can_read_all: bool = False #Whether user can read all
    can_assign: bool = False #Whether user can assign
    can_share: bool = False #Whether user can share

    class Config:
        orm_mode = True
