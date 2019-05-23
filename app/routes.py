from flask import render_template
from app import app

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
