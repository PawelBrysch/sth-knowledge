from pytest_pgsql.plugin import postgresql_db, transacted_postgresql_db


# from sqlalchemy import MetaData
# meta = MetaData()

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

ins = students.insert()

ins = students.insert().values(name='jack', lastname='Jack Jones')
a=2

engine_ = create_engine()
engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
conn = engine.connect()