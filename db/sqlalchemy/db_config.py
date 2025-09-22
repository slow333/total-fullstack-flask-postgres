from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, String, insert, Integer, ForeignKey

engine = create_engine('postgresql://postgres:1111@localhost:5432/mydb')
# engine = create_engine('postgresql://postgres:1234@192.168.219.101:5432/mydb', echo=True)
metadata = MetaData()

# create table
users = Table('users', metadata,
  Column('id', Integer, primary_key=True),
  Column('name', String(30)),
  Column('fullname', String(50))
)
addresses = Table('addresses', metadata,
  Column('id', Integer, primary_key=True),
  Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
  Column('email_address', String(100), nullable=False)
)
metadata.create_all(engine)