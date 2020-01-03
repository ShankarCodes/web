from flask import render_template
from .app import app

@app.route('/')
@app.route('/home')
def home_page():
    ctx = {'title':'Hello','username':'shankar'}
    return render_template('index.html',ctx=ctx)
