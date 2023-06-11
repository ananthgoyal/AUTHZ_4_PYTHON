from datetime import datetime
from sqlite3 import Date
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException
from Role import Role
from User import User
from item import Item
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models
#import models

app = FastAPI()

db = SessionLocal()


@app.get('/')
def index():
    return {"message": "Enable Test"}

"""Test on dummy Item class for CRUD Operations"""

"""Create Item"""
@app.post('/items', response_model=Item, status_code = status.HTTP_201_CREATED)
def createItem(item: Item):
    newItem = models.Item(
            name = item.name,
            id = item.id
    )

    db.add(newItem)
    db.commit()

    return newItem

"""Read All Items"""
@app.get('/items', response_model = List[Item], status_code = 200)
def getAllItems():
    items = db.query(models.Item).all()
    return items

"""Read Item"""
@app.get('/items/{item_id}', response_model = Item, status_code = status.HTTP_200_OK)
def getItem(item_id: int):
    foundItem = db.query(models.Item).filter(models.Item.id==item_id).first()
    return foundItem


"""Update Item"""
@app.put('/items/{item_id}', response_model = Item, status_code=status.HTTP_200_OK)
def updateItem(item_id:int, item:Item):
    foundItem = db.query(models.Item).filter(models.Item.id==item_id).first()
    foundItem.name = item.name
    foundItem.id = item.id
    db.commit()
    
    return foundItem

"""Delete Item"""
@app.delete('/items/{item_id}')
def deleteItem(item_id:int):
    deleteItem = db.query(models.Item).filter(models.Item.id == item_id).first()
    if deleteItem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Not Found")

    db.delete(deleteItem)
    db.commit()

    return deleteItem


"""Roles CRUD Operations"""

"""Create a Role"""

@app.post('/roles', response_model=Role, status_code = status.HTTP_201_CREATED)
def create_role(role: Role):
    new_role = models.Role(
            name = role.name,
            permissions = role.permissions,
            tags = role.tags,
            createdOn = datetime.now(),
            createdBy = role.createdBy,
            lastModifiedOn = datetime.now(),
            lastModifiedBy = role.lastModifiedBy,
            version = 1,
            effectiveFrom =  role.effectiveFrom,
            isEnabled = role.isEnabled,
            id = role.id
    )

    db.add(new_role)
    db.commit()

    return new_role

"""Read All Roles"""
@app.get('/roles', response_model = List[Role], status_code = 200)
def get_all_roles():
    return db.query(models.Role).all()


"""Read a Role"""
@app.get('/roles/{role_id}', response_model = Role, status_code = status.HTTP_200_OK)
def getItem(role_id: int):
    return db.query(models.Role).filter(models.Role.id==role_id).first()


"""Update Role"""
@app.put('/roles/{role_id}', response_model = Role, status_code=status.HTTP_200_OK)
def updateItem(role_id:int, role:Role):
    role_to_be_updated = db.query(models.Role).filter(models.Role.id==role_id).first()
    role_to_be_updated.name = role.name
    role_to_be_updated.permissions = role.permissions
    role_to_be_updated.tags = role.tags
    role_to_be_updated.id = role.id
    role_to_be_updated.isEnabled = role.isEnabled
    role_to_be_updated.lastModifiedOn = datetime.now()
    role_to_be_updated.version += 1
    db.commit()
    
    return role_to_be_updated

"""Delete Role"""
@app.delete('/roles/{role_id}')
def delete_role(role_id:int):
    role_to_be_deleted = db.query(models.Role).filter(models.Role.id == role_id).first()
    if role_to_be_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Not Found")

    db.delete(role_to_be_deleted)
    db.commit()

    return role_to_be_deleted


"""Permission CRUD Operations"""

"""Create a Permission"""



'''
@app.put('/roles/{role_guid}')
def updateRole(role_guid:int, role: Role):
    return { 
        'name': role.name,     
        'permissions': role.permissions,
        'tags': role.tags
    }



@app.post('/create', response_model = Persistent)
def create(obj: Persistent):
     #look up obj using obj_id and then classify which object type it is to use respective method
    if type(obj) is User:
        createUser(obj)
    elif type(obj) is Role:
        createRole(obj)
    elif type(obj) is Permission:
        createPermission(obj)

def createUser(new_user:User):
    #user = User(name, dateOfBirth)
    #generateID
    #db.add(new_user)
    pass


def createRole(role: Role):
    pass



def createPermission(permission: Permission):
    pass


@app.post('update/')
def update():
    pass

def updateUser(user_id: int):
    #locate user with user id
    user = User()
    #update user with given parameters
    
    user.updateModificationInfo() #for all updates we call this to update persistent class information
'''