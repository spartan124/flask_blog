from flask import render_template

from app import app


@app.route('/')
def index():
    animal = 'Tiger'
    return render_template('index.html', name=animal)
