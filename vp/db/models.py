from sqlalchemy import Column, String, Integer


from vp.db import Base



class Paste(Base):
    __tablename__ = 'paste'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    

class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    ext = Column(String)