#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class Persistent(BaseModel):
    """Signifies the abstract class for all persistent objects with all common attributes included"""
    createdOn: Optional[datetime] = None #The datetime stamp object the object was created on; cannot be changed once object is created
    createdBy: int = None #The ID of the User object that created this object
    lastModifiedOn: Optional[datetime] #Datetime object indicating the time stamp this object was last modified
    lastModifiedBy: int #The of ID of the User object that last edited this object
    version: Optional[int] = 0 #The version number of 
    effectiveFrom: date #Date object indicating the time this object is effective from
    isEnabled: bool = True #Whether the object is enabled; default value is True unless changed by User
    id: int #The unique ID of the object


    def updateModificationInfo(self, modifier = None):
        """Class method that is called anytime the object gets modified"""
        self.version += 1
        self.lastModifiedOn = datetime.now()
        self.lastModifiedBy = modifier
    

