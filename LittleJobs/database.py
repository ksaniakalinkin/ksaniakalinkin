from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name, email, place, jobtype, when, worker):
	user = User(name = name, email = email, place = place, jobtype = jobtype, when = when, worker = worker)
	session.add(user)
	session.commit()
	session.rollback()

def delete_user(id):
	session.query(User).filter_by(id=id).delete()
	session.commit()
  