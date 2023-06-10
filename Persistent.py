#!/usr/bin/python
#-*- coding: utf-8 -*-
from ast import mod
#import User
from datetime import datetime
from pydantic import BaseModel

class Persistent(BaseModel):
    """Signifies the abstract class for all persistent objects with all common attributes included"""
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
        self.lastModifiedBy = modifier
    

