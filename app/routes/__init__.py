from app.routes import Tag
from app import app
from flask import render_template


app.register_blueprint(Tag.blueprint)

@app.route('/')
def index():
    return render_template('index.html', title='Home')