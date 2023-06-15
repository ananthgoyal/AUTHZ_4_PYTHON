#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.objects.Persistent import Persistent
from typing import Optional

class Permission(Persistent):
    """
    Permissions specify what tasks users can perform and what features users can access.

    Note: As of now (for simplicity), the design of the permissions class has type as an attribute but will later be adjusted to be an abstract class with unique permission types as children objects.
    """
    can_create: Optional[bool] = False #Whether user can create
    can_update: Optional[bool] = False #Whether user can update
    can_delete: Optional[bool] = False #Whether user can delete
    can_read: Optional[bool] = False #Whether user can read
    can_read_all: Optional[bool] = False #Whether user can read all
    can_assign: Optional[bool] = False #Whether user can assign
    can_share: Optional[bool] = False #Whether user can share

    class Config:
        orm_mode = True
