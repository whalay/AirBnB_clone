#!/usr/bin/python3
""" 
    This is a model class User that
    inherit from  Base Model

"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
