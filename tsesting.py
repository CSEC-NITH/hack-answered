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
    question_text = db.relationship('Question', backref='user', lazy="dynamic")
    answere_text =  db.relationship('Answer', backref='user', lazy="dynamic")
    
    def __init__(self, uname, upass, email, name, roll_no, branch):
        self.uname = uname
        self.upass = upass
        self.email = email
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def __repr__(self):
        return ('<User {}>'.format(self.uname))

class UserTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagusername = db.Column(db.String(220))
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, tagusername, user):
        self.tagusername = tagusername
        self.user = user 

    def __repr__(self):
        return ('<UserTag {}>'.format(self.name))
    


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_tags = db.relationship('QuestionTag', backref='question', lazy = 'dynamic')#relatioship with question
   
    def __init__ (self,question_text,user):
        self.question_text = question_text
        self.user = user
        
    def __repr__(self):
        return ('<question {}>'.format(self.question))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer_tags= db.relationship('AnswerTag', backref='answer', lazy = 'dynamic')#relatioship with answer
    
    def __init__ (self,answer, answer_tag_id,user ):
        self.answer_text = answer_text
        self.user = user

    def __repr__(self):
        return ('<answer {}>'.format(self.answer))


class QuestionTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questiontagname = db.Column(db.String(1000))
    question_id =  db.Column(db.Integer, db.ForeignKey('question.id')) #foreign key to link with question
    
    def __init__ (self,questiontagname,question):
        self.questiontagname = questiontagname
        self.question = question

    def __repr__(self):
        return ('<questiontag {}>'.format(self.questiontagname))

class AnswerTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answertagname = db.Column(db.String(1000))
    answer_id =  db.Column(db.Integer, db.ForeignKey('answer.id'))#foreign key to link with answer
      
    def __init__ (self,answertagname,answer):
        self.answertagname = answertagname
        self.answer = answer

    def __repr__(self):
        return ('<answertag {}>'.format(self.answertagname))

if __name__=='__main__':
    db.drop_all()
    db.create_all()    



