from pyapp.routes import Account, Entry, Tag
from pyapp import pyapp
from flask import render_template


pyapp.register_blueprint(Account.blueprint)
pyapp.register_blueprint(Entry.blueprint)
pyapp.register_blueprint(Tag.blueprint)


@pyapp.route('/')
def index():
    return render_template('index.html', title='Home')


@pyapp.route('/api/v1/')
def apiRoute():
    return render_template('api.html', title='API Home')
