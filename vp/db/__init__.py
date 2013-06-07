from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os.path


from vp import app

engine = create_engine(app.config['DATABASE_URI'],
                       convert_unicode=True)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base() 
Base.query = db_session.query_property()

import vp.db.models

def init_db():
    Base.metadata.create_all(engine)
