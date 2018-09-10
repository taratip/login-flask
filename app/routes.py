from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    name = 'Max'
    num = 3
    names = ['Connor', 'Chet', 'Todd', 'Tyler', 'Fiona', 'Tara']
    return render_template('index.html', name=name, num=num, names=names)
