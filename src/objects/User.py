#!/usr/bin/python
#-*- coding: utf-8 -*-
from src.objects.Persistent import Persistent
from datetime import datetime, date
from typing import List


class User(Persistent):
    """Signifies a user of the system."""
    name: str = "" #name of the user
    dateOfBirth: date = None #date of birth of the user
    roles: List[int] = [] #List of ID's associated with the roles of the user
    
    class Config:
        orm_mode = True

