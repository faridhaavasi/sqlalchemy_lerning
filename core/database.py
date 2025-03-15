
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)


# to create tables and database (remember will be exchanged with alembic)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session= Session()

user = User(name="ali bigdeli",age=30)
session.add(user)
session.commit()

# or you can do it in bulk

users = [User(name="Maryam",age=26),User(name="arousha",age=6)]
session.add_all(users)
session.commit()


users = session.query(User).all()

print(users)

for user in users:
    print(f"User:{user.id} ,  Name:{user.name} , Age:{user.age}")



# instead use this
user = session.query(User).filter_by(id=1).one_or_none()
print(user)


# failed attempt cause of multiple objects
user = session.query(User).filter_by(age=25).one_or_none()

# get the first matching item
user = session.query(User).filter_by(id=1).first()
print(user)

# get the object we want
user = session.query(User).filter_by(id=1).one_or_none()
# current name is ali


user.name = "hossein"

print(user.name) # its changed to hossein but its not stored in database yet


# save the changes
session.commit

user = session.query(User).filter_by(id=1).one_or_none()

session.delete(user)

session.commit()