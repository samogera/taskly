from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Create SQLAlchemy engine
engine = create_engine('sqlite:///taskly.db', echo=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()

# Define User and Task models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks = relationship('Task', backref='user')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    due_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

# Create database tables
Base.metadata.create_all(engine)
