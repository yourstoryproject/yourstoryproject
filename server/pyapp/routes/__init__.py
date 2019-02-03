from pyapp.routes import Account, Entry, Tag
from pyapp import pyapp
from flask import render_template, send_from_directory
from flask_cors import CORS

# Allow CORS so client can make requests to DB
CORS(pyapp)

pyapp.register_blueprint(Account.blueprint)
pyapp.register_blueprint(Entry.blueprint)
pyapp.register_blueprint(Tag.blueprint)


@pyapp.route('/')
def index():
    return send_from_directory(pyapp.static_folder, 'index.html')

@pyapp.route('/<path:path>')
def forward(path):
    return send_from_directory(pyapp.static_folder, path)

@pyapp.route('/api/v1/')
def apiRoute():
    return render_template('api.html', title='API Home')
