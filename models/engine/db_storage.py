#!/usr/bin/python3
""" DBStorage module """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
from sqlalchemy.dialects import mysql
from sqlalchemy import exc as sa_exc
from pprintpp import pprint
import warnings

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # Get current HBNB_ENV for default dev/test connection params
        hbnb_env = 'dev'
        # 'test' if os.getenv('HBNB_ENV') == 'test' else 'dev'
        # Create a new engine to connect to mysql
        # Default: 'mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format( 
            os.getenv('HBNB_MYSQL_USER', 'hbnb_{}'.format(hbnb_env)),
            os.getenv('HBNB_MYSQL_PWD', 'hbnb_{}_pwd'.format(hbnb_env)),
            os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            os.getenv('HBNB_MYSQL_DB', 'hbnb_{}_db'.format(hbnb_env))
        ), pool_pre_ping=True)
        # Use env var HBNB_SHOW_SQL to enable query preview
        # Note: setting show_sql=True will make checker angry
        if os.getenv('HBNB_SHOW_SQL', False):
            self.__engine.echo = True
        # Drop all tables if HBNB_ENV==test
        # Tables recreated when storate.reload() called in models/__init__
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    
    def all(self, cls=None):
        """ Selects rows from mysql database """
        classes = [cls] if cls is not None else [City, State]
        result_dict = {}
        for c in classes:
            obj_query = self.__session.query(c)
            for row in obj_query.all():
                # For single-table query, row is single obj
                dict_id = "{}.{}".format(type(row).__name__, row.id)
                result_dict[dict_id] = row
        return result_dict

    def new(self, obj):
        """ Inserts a new row to table for obj """
        # Add obj -> 'INSERT INTO <table>(col1, col2, ...) VALUES(val1, val2, ...)'
        self.__session.add(obj)
        self.save()
        return obj.id

    def save(self):
        """ Commits changes to MySQL """
        # Call commit() to run the SQL to insert object
        self.__session.commit()
        self.__session.flush()

    def delete(self, obj=None):
        self.__session.query(type(obj)).filter(type(obj).id==obj.id).delete()
        self.save()

    def reload(self):
        # print(Base.metadata.tables)
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        self.save()