from flask import Flask, render_template, url_for, request, session, redirect
from flask.helpers import flash
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Fatema'
app.config['MONGO_URI'] = 'mongodb+srv://Fatema:Fatema786@login.tli64.mongodb.net/test'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if login_user['name'] == request.form['username'] and login_user['password'] == request.form['pass']:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))

        else:
            flash('*Invalid Username/Password')
            return redirect(url_for('index'))

    else:
        flash('*Invalid Username/Password')
        return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        

        if existing_user is None:
            users.insert({'name' : request.form['username'], 'password' :request.form['pass']})
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
    
    else:
        flash('Email address already exists')
        return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_page.html')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host="0.0.0.0", debug=True)
    #host="0.0.0.0"

    # elif login_user['username'] and login_user['password'] == '':
    #         flash('*Username/password cannot be empty')
    #         return redirect(url_for('index'))