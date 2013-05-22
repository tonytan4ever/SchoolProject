from flask_sqlalchemy import SQLAlchemy

from control import db,app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    message = db.Column(db.String)
    

    def __init__(self, username, message):
        self.username = username
        self.message = message