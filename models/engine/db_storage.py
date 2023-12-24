#!/usr/bin/python3
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls)

        result = []
        for obj in objs:

            better_dic = BaseModel.to_dict(obj)
            better_dic.pop("__class__")
            result.append(f"[{type(obj).__name__}] ({obj.id}) {better_dic}")

        return result

    def new(self, obj):
        """Adds new object to the storage"""
        self.__session.add(obj)

    def save(self):
        """Saves storage to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """Close the current database session."""
        self.__session.remove()