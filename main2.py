#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

def create_tables():
    # Reload the storage to create tables
    storage.reload()

if __name__ == "__main__":
    # Create empty tables
    create_tables()
