from app import app
from flask import json, render_template, Response
from app.models.Account import Account
from app.models.Entry import Entry
from app.models.Tag import Tag


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


@app.route('/api/v1/tags/<int:tagId>', methods=['GET'])
def tag(tagId):
    tag = Tag.get_tag(tagId)

    if not tag:
        return server_response({'error': 'Tag not found'}, 404)

    response = {'tag': tag.to_json()}

    return server_response(response, 200)