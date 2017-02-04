# from app import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

if __name__=='__main__':
    from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True)
    upass = db.Column(db.String(20))
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    comment = db.Column(db.String(20))
    # date = db.Column(db.Date)
    # roll_no = db.Column(db.String(20), unique=True)

    def __init__(self, uname, upass, email, phone,comment):
        self.uname = uname
        self.upass = upass
        self.email = email
        self.phone = phone
        self.comment = comment
        # self.roll_no = roll_no

    def __repr__(self):
        return ('<User {}>'.format(self.uname))

# class Posts(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # post_text = db.Column(db.String(220))
    # user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
    


if __name__=='__main__':
    db.drop_all()
    db.create_all()

