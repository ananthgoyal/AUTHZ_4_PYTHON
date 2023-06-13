from datetime import datetime
from math import perm
from sqlite3 import Date
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException
from src.objects.Role import Role
from src.objects.User import User
from src.objects.Permission import Permission
from pydantic import BaseModel
from typing import Optional, List
from src.database import SessionLocal
import src.models as models

app = FastAPI()

db = SessionLocal()


@app.get('/')
def index():
    return {"message": "CRUD Test"}

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
@app.post('/permissions', response_model=Permission, status_code = status.HTTP_201_CREATED)
def create_permission(permission: Permission):
    new_permission = models.Permission(
            can_create = permission.can_create,
            can_update = permission.can_update,
            can_delete = permission.can_delete,
            can_read = permission.can_delete,
            can_read_all = permission.can_read_all,
            can_assign = permission.can_assign,
            can_share = permission.can_share,
            createdOn = datetime.now(),
            createdBy = permission.createdBy,
            lastModifiedOn = datetime.now(),
            lastModifiedBy = permission.lastModifiedBy,
            version = 1,
            effectiveFrom =  permission.effectiveFrom,
            isEnabled = permission.isEnabled,
            id = permission.id
    )

    db.add(new_permission)
    db.commit()

    return new_permission

"""Read All Permission"""
@app.get('/permissions', response_model = List[Permission], status_code = 200)
def get_all_roles():
    return db.query(models.Permission).all()

"""Read Single Permission"""
@app.get('/permissions/{permission_id}', response_model = Permission, status_code = status.HTTP_200_OK)
def get_permission(permission_id: int):
    return db.query(models.Permission).filter(models.Permission.id==permission_id).first()

"""Update Permission"""
@app.put('/perissions/{permission_id}', response_model = Permission, status_code=status.HTTP_200_OK)
def update_permission(permission_id:int, permission:Permission):
    perm_to_be_updated = db.query(models.Permission).filter(models.Permission.id==permission_id).first()
    perm_to_be_updated.can_create = permission.can_create
    perm_to_be_updated.can_update = permission.can_update
    perm_to_be_updated.can_delete = permission.can_delete
    perm_to_be_updated.can_read = permission.can_read
    perm_to_be_updated.can_read_all = permission.can_read_all
    perm_to_be_updated.can_assign = permission.can_assign
    perm_to_be_updated.can_share = permission.can_share
    perm_to_be_updated.id = permission.id
    perm_to_be_updated.isEnabled = perm.isEnabled
    perm_to_be_updated.lastModifiedOn = datetime.now()
    perm_to_be_updated.version += 1
    db.commit()
    
    return perm_to_be_updated

"""Delete a Permission"""
@app.delete('/permissions/{permission_id}')
def delete_permission(permission_id:int):
    perm_to_be_deleted = db.query(models.Permission).filter(models.Permission.id == permission_id).first()
    if perm_to_be_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Not Found")

    db.delete(perm_to_be_deleted)
    db.commit()

    return perm_to_be_deleted

"""CRUD Operations for User"""

"""Create a User"""
@app.post('/users', response_model=User, status_code = status.HTTP_201_CREATED)
def create_user(user: User):
    new_user = models.User(
            name = user.name,
            dateOfBirth = user.dateOfBirth,
            roles = user.roles,
            createdOn = datetime.now(),
            createdBy = user.createdBy,
            lastModifiedOn = datetime.now(),
            lastModifiedBy = user.lastModifiedBy,
            version = 1,
            effectiveFrom =  user.effectiveFrom,
            isEnabled = user.isEnabled,
            id = user.id
    )

    db.add(new_user)
    db.commit()

    return new_user

"""Read All Users"""
@app.get('/users', response_model = List[User], status_code = 200)
def get_all_users():
    return db.query(models.User).all()

"""Read Single User"""
@app.get('/users/{user_id}', response_model = User, status_code = status.HTTP_200_OK)
def get_permission(user_id: int):
    return db.query(models.User).filter(models.User.id==user_id).first()

"""Update User"""
@app.put('/users/{user_id}', response_model = User, status_code=status.HTTP_200_OK)
def update_user(user_id:int, user:User):
    user_to_be_updated = db.query(models.User).filter(models.User.id==user_id).first()
    user_to_be_updated.name = user.name
    user_to_be_updated.dateOfBirth = user.dateOfBirth
    user_to_be_updated.roles = user.roles,    
    user_to_be_updated.can_assign = user.can_assign
    user_to_be_updated.can_share = user.can_share
    user_to_be_updated.id = user.id
    user_to_be_updated.isEnabled = user.isEnabled
    user_to_be_updated.lastModifiedOn = datetime.now()
    user_to_be_updated.version += 1
    db.commit()
    
    return user_to_be_updated

"""Delete a User"""
@app.delete('/users/{user_id}')
def delete_user(user_id:int):
    user_to_be_deleted = db.query(models.User).filter(models.User.id == user_id).first()
    if user_to_be_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Not Found")

    db.delete(user_to_be_deleted)
    db.commit()

    return user_to_be_deleted
