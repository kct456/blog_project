from FlaskBlog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    major = db.Column(db.String(120), db.ForeignKey('major.name'))

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.major}')"

class Major(db.Model):
    name = db.Column(db.String(120), unique=True,nullable=False, primary_key=True)
    fromCC = db.Column(db.String(120), nullable = False)
    toUC = db.Column(db.String(120), nullable = False)
    student = db.relationship('User',backref='student',lazy=True)
    c1 = db.Column(db.String(120))
    c1e = db.Column(db.String(120))
    c2 = db.Column(db.String(120))
    c2e = db.Column(db.String(120))
    c3 = db.Column(db.String(120))
    c3e = db.Column(db.String(120))
    c4 = db.Column(db.String(120))
    c4e = db.Column(db.String(120))
    c5 = db.Column(db.String(120))
    c5e = db.Column(db.String(120))
    c6 = db.Column(db.String(120))
    c6e = db.Column(db.String(120))
    c7 = db.Column(db.String(120))
    c7e = db.Column(db.String(120))
    c8 = db.Column(db.String(120))
    c8e = db.Column(db.String(120))
    c9 = db.Column(db.String(120))
    c9e = db.Column(db.String(120))
    c10 = db.Column(db.String(120))
    c10e = db.Column(db.String(120))

    def __repr__(self):
        return f"Major('{self.name}','{self.student}','{self.fromcc}','{self.toUC}','{self.c1}','{self.c2}','{self.c3}','{self.c4}','{self.c5}','{self.c6}','{self.c7}','{self.c8}','{self.c9}','{self.c10}','{self.c1e}','{self.c2e}','{self.c3e}','{self.c4e}','{self.c5e}','{self.c6e}','{self.c7e}','{self.c8e}','{self.c9e}','{self.c10e}')"
