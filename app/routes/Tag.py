from app.utils.server import parse_response
from app.models import Tag
from app.api.Tag import create_tag, get_tag, get_tags
from flask import Blueprint, jsonify


blueprint = Blueprint('tags', __name__, url_prefix='/api/v1/tags')

@blueprint.route('/', methods=['GET'])
def tags():
    response = get_tags()

    return parse_response(response, response["status_code"])

@blueprint.route('/<int:tagId>', methods=['GET'])
def tag(tagId):
    response = get_tag(tagId)

    return parse_response(response, response["status_code"])

@blueprint.route('/create/<string:tagName>', methods=['POST'])
def add_tag(tagName):
    response = create_tag(tagName)

    return parse_response(response, response["status_code"])