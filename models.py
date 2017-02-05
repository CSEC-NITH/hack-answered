# from app import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

if __name__=='__main__':
    from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), unique=True)
    upass = db.Column(db.String(30))
    email = db.Column(db.String(30))
    name = db.Column(db.String(30))
    roll_no = db.Column(db.String(20))
    branch = db.Column(db.String(30))
    # date_of_join = db.Column(db.DateTime())
    usertags = db.relationship('UserTag', backref='user', lazy="dynamic")
    questiontag = db.relationship('QuestionTag', backref='user', lazy="dynamic")
    
    def __init__(self, uname, upass, email, name, roll_no, branch):
        self.uname = uname
        self.upass = upass
        self.email = email
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def __repr__(self):
        return ('<User {}>'.format(self.uname))

class QuestionTag(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
      
    def __init__ (self,question,user):
        self.question = question
        self.user = user 

    def __repr__(self):
        return ('<questiontag {}>'.format(self.question))

     
class UserTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(220))
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, user):
        self.name = name
        self.user = user 

    def __repr__(self):
        return ('<UserTag {}>'.format(self.name))


if __name__=='__main__':
    db.drop_all()
    db.create_all()

