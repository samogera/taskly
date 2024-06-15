from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///taskly.db')
Session = sessionmaker(bind=engine)
session = Session()

