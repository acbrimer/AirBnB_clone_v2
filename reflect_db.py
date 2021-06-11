#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import select
import sqlalchemy.schema as schema
from sqlalchemy.schema import CreateTable
from sqlalchemy.ext.declarative import declarative_base
import os

# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session

""" sqlalchemy MySQL connection with env vars """ 
engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format( 
    os.getenv('HBNB_MYSQL_USER', 'root'),
    os.getenv('HBNB_MYSQL_PWD', 'Bladyblird01'),
    os.getenv('HBNB_MYSQL_HOST', 'localhost'),
    os.getenv('HBNB_MYSQL_DB', 'hbtn_airbnb_reflect')
    ))

Base = declarative_base()
Base.metadata.reflect(engine)

for tbl_name in Base.metadata.tables:
    print("#!/usr/bin/python3")
    print("\"\"\" Module for `{}` class \"\"\"".format(tbl_name.capitalize()))
    print("")
    print()
    print()
    print("class {}(Base):".format(tbl_name.capitalize()))
    print("    \"\"\" Declaritive model for `{}` table \"\"\"".format(tbl_name))
    print("    __tablename__ = '{}'".format(tbl_name))
    tbl = Base.metadata.tables[tbl_name]
    cols = tbl.__dict__['_columns']
    for col in cols:
        # pprint(col.__dict__)
        col_params = {"nullable":'nullable'}
        if col.__dict__['primary_key']:
            col_params['primary_key'] = True
        if col.__dict__['default']:
            col_params['default'] = col.__dict__['default']
        col_param_list = []
        col_type = str(col.__dict__['type']).replace('VARCHAR', 'String').replace('INTEGER(11)', 'Integer').capitalize()
        col_param_list.append(str(col_type))
        if col.__dict__['foreign_keys']:
            col_param_list.append(str(col.__dict__['foreign_keys'])[1:-1])
        col_param_list.extend([str("{} = {}".format(k, col.__dict__[k])) for k in col_params])
        col_param_str = ", ".join(col_param_list)
        print("    {} = Column({})".format(col.__dict__['name'], col_param_str))
    print()
    print("-" * 80)
