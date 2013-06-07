from flask import Flask
import os.path


app = Flask(__name__)
app.config.from_object('vpconfig')
app.secret_key = app.config['ENTROPY']


from vp.db import db_session, init_db, engine, Base

if not os.path.exists(app.config['DB_PATH']):
    init_db()
    

@app.teardown_request
def remove_db_session(exception):
    db_session.commit()
    db_session.remove()


from vp.views import rest

app.register_blueprint(rest.mod)