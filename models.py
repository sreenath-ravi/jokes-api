from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)
    joke = Column(String, nullable=True) 
    setup = Column(String, nullable=True)
    delivery = Column(String, nullable=True)
    nsfw = Column(Boolean, nullable=False)
    political = Column(Boolean, nullable=False)
    sexist = Column(Boolean, nullable=False)
    safe = Column(Boolean, nullable=False)
    lang = Column(String, nullable=False)
