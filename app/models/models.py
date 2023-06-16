from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    contact = db.Column(db.String)
    role = db.Column(db.String)

    def is_admin(self):
        if self.role == 'admin':
            return True
        return False

