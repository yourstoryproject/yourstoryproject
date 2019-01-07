from app.utils.server import server_response
from app.models.Tag import Tag
from flask import Blueprint


blueprint = Blueprint('tags', __name__, url_prefix='/api/v1/tags')

@blueprint.route('/', methods=['GET'])
def tags():
    tags = Tag.get_tags()

    response = {'tags': [tag.to_json() for tag in tags]}

    return server_response(response, 200)


@blueprint.route('/<int:tagId>', methods=['GET'])
def tag(tagId):
    tag = Tag.get_tag(tagId)

    if not tag:
        return server_response({'error': 'Tag not found'}, 404)

    response = {'tag': tag.to_json()}

    return server_response(response, 200)