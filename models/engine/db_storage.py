#!/usr/bin/python3
""" Defines The DBStorage engine"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """MySQL Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize a DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database session"""
        objectsDict = dict()
        if cls is None:
            listClasses = [Amenity, City, Place, State, Review, User]
            for class_ in listClasses:
                try:
                    query = self.__session.query(class_).all()
                    for object_ in query:
                        className = object_.to_dict()['__class__']
                        id_ = object_.id
                        classId = className + "." + id_
                        objectsDict[classId] = object_
                except Exception:
                    pass
        else:
            query = self.__session.query(cls).all()
            for object_ in query:
                className = object_.to_dict()['__class__']
                id_ = object_.id
                classId = className + "." + id_
                objectsDict[classId] = object_
        return objectsDict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call close"""
        self.__session.close()
