#!/usr/bin/python3
"""This is the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User:
        BaseModel class nheretar
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
