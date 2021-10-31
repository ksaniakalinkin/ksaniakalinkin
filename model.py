from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	email = Column(String)
	place = Column(String)
	jobtype = Column(String)
	when = Column(String)
	worker = Column(String)