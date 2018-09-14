from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    def set_password(self, password):
        # generate_password_hash generates password hash with 256 long characters
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # check if password entered in the form matched with password generated by user
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'Name {}: Email - {}'.format(self.name, self.email)

# For loading user information in session


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
