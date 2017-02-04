from flask import Flask, render_template
from flask import flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request
from models import User
app = Flask(__name__, static_url_path='/static')
app.secret_key = "some_key"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'

db = SQLAlchemy(app)

# @app.route('/')
# def home_page():
    # return render_template('base.html')

# @app.route('/user/<nam>')
# def profile_page(nam):
    # return render_template('profile.html', name=nam)

# @app.route('/all_users')
# def all_users():
    # users = User.query.all()
    # print(users)
    # return render_template('users.html', users=users)

# @app.route('/new', methods = ['GET', 'POST'])
# def new():
   # if request.method == 'POST':
      # if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         # flash('Please enter all the fields', 'error')
      # else:
         # user = User(request.form['id'], request.form['city'],
            # request.form['addr'], request.form['pin'])
         
         # db.session.add(user)
         # db.session.commit()
         # flash('Record was successfully added')
         # return redirect(url_for('show_all'))
   # return render_template('new.html')

@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/login', methods = ['POST'])
def sigin():
    print("GOT A POST OF DATA !!!")
    uname = request.form['uname']
    upass = request.form['upass']
    the_user = User.query.filter_by(uname=uname).first()
    print(uname,upass)
    if the_user == None:
        error = 'USER NAME NOT FOUND'
        flash(error)
        return redirect('/')
    print(the_user, the_user.uname, the_user.upass)
    if the_user.upass == upass:
        msg = 'PASSWORD MATCH'
    else:
        msg = 'PASSWORD not match'
    flash(msg)
    return redirect('/')
    # return redirect(url_for('all_users'))

@app.route('/signup', methods = ['POST'])
def signup():
    print("GOT A POST OF DATA !!!")
    user = User(request.form['uname'], request.form['upass'],
    request.form['email'], request.form['phone'], request.form['comment'])

    print(user)
    db.session.add(user)
    db.session.commit()
    print('Record was successfully added')
    return redirect(url_for('all_users'))


if __name__=='__main__':
    app.run()
