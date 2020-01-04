
from sqlalchemy import Table, MetaData, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pytest_pgsql.plugin import postgresql_db

my_table = Table('abc', MetaData(), Column('def', Integer()))

# A declarative model works too.
class MyORMModel(declarative_base()):
    id = Column(Integer, primary_key=True)

# Pass a variable amount of tables to create
postgresql_db.create_table(my_table, MyORMModel)