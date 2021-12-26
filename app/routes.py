
#Imports
from flask.helpers import url_for
from werkzeug.utils import redirect
from app import app
from flask import render_template, flash, redirect
from datetime import date
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)