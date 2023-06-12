#!/usr/bin/python
#-*- coding: utf-8 -*-
from ast import mod
#from User import User
#import User
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class Persistent(BaseModel):
    """Signifies the abstract class for all persistent objects with all common attributes included"""
    createdOn: Optional[datetime]
    createdBy: int
    lastModifiedOn: Optional[datetime]
    lastModifiedBy: int
    version: Optional[int]
    effectiveFrom: date
    isEnabled: bool
    id: int

    '''class Config:
        arbitrary_types_allowed = True

        
    def __init__(self):
        self.createdOn = None
        self.createdBy = None
        self.lastModifiedOn = None
        self.lastModifiedBy = None
        self.version = None
        self.effectiveFrom = None
        self.isEnabled = None
        self.id = None


    def updateModificationInfo(self, modifier = None):
        self.version += 1
        self.lastModifiedOn = datetime.now()
        self.lastModifiedBy = modifier'''
    

