from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Jeremy'}
    posts = [
        {
            'author': {'username': 'Wise Matt'},
            'body': 'Hooray for space!'
        },
        {
            'author': {'username': 'Smart Matt'},
            'body': 'Python is cool.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
