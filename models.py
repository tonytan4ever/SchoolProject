from control import db,app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String)
    
    
    email = db.Column(db.String(120), unique=True)
    
    

    def __init__(self, username, message):
        self.username = username
        self.message = message