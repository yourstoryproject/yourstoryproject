from app.routes import Account, Tag
from app import app
from flask import render_template


app.register_blueprint(Tag.blueprint)
app.register_blueprint(Account.blueprint)

@app.route('/')
def index():
    return render_template('index.html', title='Home')