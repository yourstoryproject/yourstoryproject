from app import app
from flask import json, render_template, Response
from app.models import Entry, Tag

def server_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/api/v1/tags', methods=['GET'])
def tags():
    tags = Tag.get_tags()

    response = {'tags': [tag.to_json() for tag in tags]}

    return server_response(response, 200)