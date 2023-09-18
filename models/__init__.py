#!/usr/bin/python3
"""__init__magic method for model sdirectory"""
from models.engine.file_storage import FileStorage

store = FileStorage()
store.reload()
