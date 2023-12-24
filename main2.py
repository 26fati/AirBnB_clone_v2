#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review

def create_tables():
    # Reload the storage to create tables
    storage.reload()

if __name__ == "__main__":
    # Create empty tables
    create_tables()
