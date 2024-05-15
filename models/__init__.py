#!/usr/bin/python3
"""
Module: __init__ module for AirBnB_clone project 
 
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()