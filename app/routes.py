
#Imports
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.urls import url_parse
from app import app, db
from flask import render_template, flash, redirect, request
from datetime import date
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Max'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Bitcoin hits $100k',
            'date': f'{date.today()}'
        },
        {
            'author': {'username': 'Charles'},
            'body': 'Ethereum to $20k EOY?',
            'date': f'{date.today()}'
        },
        {
            'author': {'username': 'Richard'},
            'body': 'Bears are back in full force!',
            'date': f'{date.today()}'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
