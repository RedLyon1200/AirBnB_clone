#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
classes = {
    'BaseModel': BaseModel,
    'Test': 'Test'
}
storage = FileStorage()
storage.reload()
