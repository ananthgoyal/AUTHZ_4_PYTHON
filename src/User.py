#!/usr/bin/python
#-*- coding: utf-8 -*-
from src.Persistent import Persistent
from datetime import datetime, date
from typing import List


class User(Persistent):
    """Signifies a user of the system."""
    name: str
    dateOfBirth: date
    roles: List[int]
    
    class Config:
        orm_mode = True

