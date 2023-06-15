#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel
import uuid

class Persistent(BaseModel):
    """Signifies the abstract class for all persistent objects with all common attributes included"""
    createdOn: Optional[datetime] = None #The datetime stamp object the object was created on; cannot be changed once object is created
    createdBy: Optional[str] = None #The ID of the User object that created this object
    lastModifiedOn: Optional[datetime]  = None#Datetime object indicating the time stamp this object was last modified
    lastModifiedBy: Optional[str] = None #The of ID of the User object that last edited this object
    version: Optional[int] = 0 #The version number of the object
    effectiveFrom: Optional[date] = None #Date object indicating the time this object is effective from
    isEnabled: Optional[bool] = True #Whether the object is enabled; default value is True unless changed by User
    id: Optional[str] = None #The unique ID of the object


    def updateModificationInfo(self, modifier = None):
        """Class method that is called anytime the object gets modified"""
        self.version += 1
        self.lastModifiedOn = datetime.now()
        self.lastModifiedBy = modifier
    

